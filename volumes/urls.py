# -*- coding: utf-8 -*-

from django.conf.urls import url
from volumes import views

urlpatterns = (
    url(r'^volume_list/$', views.volume_list, name='volume_list'),
    url(r'^get_volume_list/$', views.get_volume_list, name='get_volume_list'),
)