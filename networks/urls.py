# -*- coding: utf-8 -*-

from django.conf.urls import url
from networks import views

urlpatterns = (
    url(r'^network_list/(?P<pk>[0-9]+)/$', views.network_list, name='network_list'),
    url(r'^get_network_list/$', views.get_network_list, name='get_network_list'),
)