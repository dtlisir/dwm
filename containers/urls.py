# -*- coding: utf-8 -*-

from django.conf.urls import url
from containers import views

urlpatterns = (
    url(r'^container_list/$', views.container_list, name='container_list'),
    url(r'^get_container_list/$', views.get_container_list, name='get_container_list'),
    url(r'^container_create/$', views.container_create, name='container_create'),
    url(r'^container_detail/(?P<id>[0-9a-zA-Z]+)/$', views.container_detail, name='container_detail'),
    url(r'^container_detail/(?P<id>[0-9a-zA-Z]+)/$', views.container_detail, name='container_detail'),
)