"""
URL configuration for the CEDA services app.
"""

__author__ = "Rhys Evans"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"

from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import MyServicesView

urlpatterns = [
    # The root pattern redirects to my_services
    path('',RedirectView.as_view(pattern_name = 'my_services')),
    path('my_services/', MyServicesView.as_view(), name = 'my_services'),

]
