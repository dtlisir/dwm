# -*- coding: utf-8 -*-

from django.conf.urls import url
from hosts import views

urlpatterns = (
    url(r'^node_list/$', views.node_list, name='node_list'),
    url(r'^get_node_list/$', views.get_node_list, name='get_node_list'),
    url(r'^test_node_conn/$', views.test_node_conn, name='test_node_conn'),
    url(r'^node_create/$', views.node_create, name='node_create'),
    url(r'^post_create_node/$', views.post_create_node, name='post_create_node'),
    url(r'^node_edit/(?P<pk>[0-9]+)/$', views.node_edit, name='node_edit'),
    url(r'^post_edit_node/$', views.post_edit_node, name='post_edit_node'),
    url(r'^node_del/$', views.node_del, name='node_del'),
    url(r'^node_detail/(?P<pk>[0-9]+)/$', views.node_detail, name='node_detail'),

    url(r'^group_list/$', views.group_list, name='group_list'),
    url(r'^get_group_list/$', views.get_group_list, name='get_group_list'),
    url(r'^group_create/$', views.group_create, name='group_create'),
    url(r'^post_create_group/$', views.post_create_group, name='post_create_group'),
    url(r'^group_edit/(?P<pk>[0-9]+)/$', views.group_edit, name='group_edit'),
    url(r'^post_edit_group/$', views.post_edit_group, name='post_edit_group'),
    url(r'^group_del/$', views.group_del, name='group_del'),
)
