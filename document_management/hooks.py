# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "document_management"
app_title = "Document Management"
app_publisher = "www.fwrat.com"
app_description = "Document Management App by Fwrat.com"
app_icon = "octicon octicon-book"
app_color = "#42ACF1"
app_email = "admin@fwrat.com"
app_license = "MIT"
fixtures = ["Custom Field","Custom Script","Print Format", "Translation", "Document Record Template","Language"]
# fixtures = [{"doctype": "DocType","filters": { "custom" : ["=", "1"]}},"Custom Field","Custom Script","Print Format"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/document_management/css/document_management.css"
# app_include_js = "/assets/document_management/js/document_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/document_management/css/document_management.css"
# web_include_js = "/assets/document_management/js/document_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "document_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "document_management.install.before_install"
# after_install = "document_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "document_management.notifications.get_notification_config"

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
# 		"document_management.tasks.all"
# 	],
# 	"daily": [
# 		"document_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"document_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"document_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"document_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "document_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "document_management.event.get_events"
# }

