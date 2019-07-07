# -*- coding: utf-8 -*-

from django.conf.urls import url
from networks import views

urlpatterns = (
    url(r'^network_list/$', views.network_list, name='network_list'),
)