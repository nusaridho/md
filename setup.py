# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in midtrans/__init__.py
from midtrans import __version__ as version

setup(
	name='midtrans',
	version=version,
	description='Midtrans Payment Gateway',
	author='NDK',
	author_email='develop@ridhosribumi.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
