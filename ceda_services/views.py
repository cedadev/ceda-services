"""
Module defining views for the JASMIN services app.
"""

__author__ = "Matt Pryor"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"

import logging
import functools
import socket
from datetime import date

from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


_log = logging.getLogger(__name__)

class MyServicesView(TemplateView):
    """
    Handler for ``/my_services/``.

    Responds to GET requests only. The user must be authenticated.

    Displays all of the services for which the user has an active grant or request.
    """
    template_name = 'ceda_services/my_services.html'
