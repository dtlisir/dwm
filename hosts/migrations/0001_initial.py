# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-16 08:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='名称')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='创建者')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('comment', models.TextField(blank=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '主机组',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HostNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='名称')),
                ('url', models.CharField(max_length=128, unique=True, verbose_name='URL')),
                ('ip', models.CharField(blank=True, max_length=32, verbose_name='IP')),
                ('comment', models.TextField(blank=True, verbose_name='备注')),
                ('created_by', models.CharField(blank=True, max_length=32, verbose_name='创建者')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('os', models.CharField(blank=True, max_length=128, verbose_name='操作系统')),
                ('os_arch', models.CharField(blank=True, max_length=16, verbose_name='架构')),
                ('cpu_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='CPU核数')),
                ('memory', models.IntegerField(blank=True, default=0, null=True, verbose_name='内存总量')),
                ('active', models.BooleanField(default=False, verbose_name='状态')),
                ('c_running', models.IntegerField(blank=True, default=0, null=True, verbose_name='运行数')),
                ('c_paused', models.IntegerField(blank=True, default=0, null=True, verbose_name='暂停数')),
                ('c_stopped', models.IntegerField(blank=True, default=0, null=True, verbose_name='停止数')),
                ('check_time', models.DateTimeField(auto_now=True, verbose_name='检测时间')),
                ('d_version', models.CharField(blank=True, max_length=32, verbose_name='Docker版本')),
                ('c_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='容器数')),
                ('i_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='镜像数')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nodes', to='hosts.HostGroup', verbose_name='组名')),
                ('users', models.ManyToManyField(blank=True, related_name='nodes', to=settings.AUTH_USER_MODEL, verbose_name='授权用户')),
            ],
            options={
                'verbose_name': '主机',
            },
        ),
    ]
