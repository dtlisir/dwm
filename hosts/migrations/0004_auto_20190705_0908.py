# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-05 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_auto_20190705_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostnode',
            name='c_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='容器数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='c_paused',
            field=models.IntegerField(blank=True, null=True, verbose_name='暂停数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='c_running',
            field=models.IntegerField(blank=True, null=True, verbose_name='运行数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='c_stopped',
            field=models.IntegerField(blank=True, null=True, verbose_name='停止数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='cpu_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='CPU核数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='i_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='镜像数'),
        ),
        migrations.AlterField(
            model_name='hostnode',
            name='memory',
            field=models.IntegerField(blank=True, null=True, verbose_name='内存总量'),
        ),
    ]
