# -*- coding: utf-8 -*-

from django.conf.urls import url
from containers import views

urlpatterns = (
    url(r'^container_list/(?P<pk>[0-9]+)/$', views.container_list, name='container_list'),
    url(r'^get_container_list/$', views.get_container_list, name='get_container_list'),
    url(r'^container_create/(?P<pk>[0-9]+)/$', views.container_create, name='container_create'),
    url(r'^container_detail/(?P<pk>[0-9]+)/(?P<id>[\w]+)/$', views.container_detail, name='container_detail'),
    url(r'^post_container_start/$', views.post_container_start, name='post_container_start'),
    url(r'^post_container_stop/$', views.post_container_stop, name='post_container_stop'),
    url(r'^post_container_restart/$', views.post_container_restart, name='post_container_restart'),
    url(r'^post_container_pause/$', views.post_container_pause, name='post_container_pause'),
    url(r'^post_container_create/$', views.post_container_create, name='post_container_create'),
    url(r'^post_container_remove/$', views.post_container_remove, name='post_container_remove'),
)