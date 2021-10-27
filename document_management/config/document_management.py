from __future__ import unicode_literals
from frappe import _
"""

Adding doctypes and displaying it 
		{
			"label": _("Custom Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Ledger",
					"doctype": "Stock Ledger Entry",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Stock Balance",
					"doctype": "Stock Ledger Entry"
				},

			]
		},
		
		{
			"label": _("Production"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Production Order",
					"description": _("Orders released for production."),
				},
				
			]
		}
		
"""
		
# this allows customization
def get_data():
	return [
		{
			"label": _("Help"),
			"icon": "fa fa-facetime-video",
			"items": [
				{
					"type": "help",
					"label": _("How to Use"),
					"youtube_id": "uqgQ-e9AZHU",
					"name": "How to use"
				},	
	
				
			]
		}
		
	]