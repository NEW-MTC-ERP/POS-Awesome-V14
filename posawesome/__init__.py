# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = "4.1.1"


def console(*data):
    # Import frappe locally within the function to avoid module-level import
    import frappe
    frappe.publish_realtime("toconsole", data, user=frappe.session.user)