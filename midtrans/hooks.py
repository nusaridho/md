# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "midtrans"
app_title = "Midtrans"
app_publisher = "NDK"
app_description = "Midtrans Payment Gateway"
app_icon = "fa fa-credit-card"
app_color = "orange"
app_email = "develop@ridhosribumi.com"
app_license = "NDK"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/midtrans/css/midtrans.css"
# app_include_js = "/assets/midtrans/js/midtrans.js"

# include js, css files in header of web template
# web_include_css = "/assets/midtrans/css/midtrans.css"
# web_include_js = "/assets/midtrans/js/midtrans.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "midtrans.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "midtrans.install.before_install"
# after_install = "midtrans.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "midtrans.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"midtrans.tasks.all"
# 	],
# 	"daily": [
# 		"midtrans.tasks.daily"
# 	],
# 	"hourly": [
# 		"midtrans.tasks.hourly"
# 	],
# 	"weekly": [
# 		"midtrans.tasks.weekly"
# 	]
# 	"monthly": [
# 		"midtrans.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "midtrans.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "midtrans.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "midtrans.task.get_dashboard_data"
# }

