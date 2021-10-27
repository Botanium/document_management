# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in document_management/__init__.py
from document_management import __version__ as version

setup(
	name='document_management',
	version=version,
	description='Document Management App by Fwrat.com',
	author='www.fwrat.com',
	author_email='admin@fwrat.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True
)
