# -*- coding: utf-8 -*-
# Copyright (c) 2019, NDK and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.integrations.utils import create_request_log, create_payment_gateway
from frappe.utils import call_hook_method
import hashlib, json
import midtransclient

class MidtransSettings(Document):
	supported_currencies = ["IDR"]

	def validate(self):
		create_payment_gateway("Midtrans")
		call_hook_method('payment_gateway_enabled', gateway="Midtrans")

	def validate_transaction_currency(self, currency):
		if currency not in self.supported_currencies:
			frappe.throw(_("Please select another payment method. Midtrans does not support transactions in currency '{0}'").format(currency))

	def get_payment_url(self, **kwargs):
		snap = midtransclient.Snap(
			is_production=bool(self.is_production),
			server_key=self.server_key,
			client_key=self.client_key
			)
		param = {}
		param.update({
				"transaction_details": {
					"order_id": kwargs['reference_docname'],
					"gross_amount": kwargs['amount']
				}, "credit_card":{
					"secure" : True
					}
				})
		try:
			trans = snap.create_transaction(param)
			payment_url = trans['redirect_url']
			doc = frappe.get_doc("Midtrans Settings")
			md5 = hashlib.md5()
			md5.update(("{}-{}".format(doc.merchant_id, kwargs['reference_docname']).encode("utf8")))
			token = md5.hexdigest()

			# kwargs.update({
			# 	"token": token
			# })

			create_request_log(kwargs, "Remote", "Midtrans", token)

			print ("Payment url : {}".format(payment_url))
			frappe.msgprint("Payment url : {}".format(payment_url))

			return payment_url

		except Exception as e:
			# frappe.msgprint(_(str(e)), raise_exception=1, indicator='red')
			raise frappe.ValidationError(str(e))


@frappe.whitelist(allow_guest=True)
def handling():
	try:
		d = frappe.local.form_dict
		md5 = hashlib.md5()
		md5.update(("{}-{}".format(d['merchant_id'], d['order_id']).encode("utf8")))
		token = md5.hexdigest()
		data = get_transaction_details(token)
		if d['transaction_status'] == "capture":
			update_integration_request_status(token, d, "Completed")
			if data.get("reference_doctype") and data.get("reference_docname"):
				custom_redirect_to = frappe.get_doc(data.get("reference_doctype"),
					data.get("reference_docname")).run_method("on_payment_authorized", "Completed")
				frappe.db.commit()
				print (data)
		elif d['transaction_status'] == "pending":
			update_integration_request_status(token, d, "Queued")
		elif d['transaction_status'] == "settlement":
			update_integration_request_status(token, d, "Completed")
		else:
			update_integration_request_status(token, d, "Failed")

		frappe.local.response.http_status_code = 200

	except Exception:
		frappe.log_error(frappe.get_traceback())

def update_integration_request_status(token, data, status, error=False, doc=None):
	if not doc:
		doc = frappe.get_doc("Integration Request", token)
	doc.update_status(data, status)

def get_transaction_details(token):
	integration_request = frappe.get_doc("Integration Request", token)
	data = json.loads(integration_request.data)
	return data
