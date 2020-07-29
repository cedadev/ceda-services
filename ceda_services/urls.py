"""
URL configuration for the CEDA services app.
"""

__author__ = "Rhys Evans"
__copyright__ = "Copyright 2015 UK Science and Technology Facilities Council"

from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views

app_name = 'ceda_services'
urlpatterns = [
    # The root pattern redirects to my_services
    path('',
        RedirectView.as_view(pattern_name = 'ceda_services:my_services'),
        name = 'service_root'),
    path('my_services/', views.my_services, name = 'my_services'),

]
