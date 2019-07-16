# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from hosts.models import HostNode
from blueapps.account.models import User
from syslogs.models import Log
from django.db.models.aggregates import Sum


def index(request):
    if not request.user.is_superuser:
        return redirect('home:index_user')
    nodes = HostNode.objects.all()
    host_count = nodes.count()
    user_count = User.objects.all().count()
    container_totle = nodes.aggregate(totles=Sum('c_count'))
    container_running = nodes.aggregate(totles=Sum('c_running'))
    container_stopped = nodes.aggregate(totles=Sum('c_stopped'))
    container_paused = nodes.aggregate(totles=Sum('c_paused'))
    container_count = container_totle['totles']
    c_running_count = container_running['totles']
    c_stopped_count = container_stopped['totles']
    c_paused_count = container_paused['totles']
    image_totle = nodes.aggregate(totles=Sum('i_count'))
    image_count = image_totle['totles']
    c_create_count = Log.objects.filter(type='CONTAINER').filter(state=True).filter(action='CREATE').count()
    c_start_count = Log.objects.filter(type='CONTAINER').filter(state=True).filter(action='START').count()
    c_stop_count = Log.objects.filter(type='CONTAINER').filter(state=True).filter(action='STOP').count()
    c_restart_count = Log.objects.filter(type='CONTAINER').filter(state=True).filter(action='RESTART').count()
    c_remove_count = Log.objects.filter(type='CONTAINER').filter(state=True).filter(action='REMOVE').count()

    context = {
        'nodes': nodes,
        'host_count': host_count,
        'user_count': user_count,
        'container_count': container_count,
        'image_count': image_count,
        'c_create_count': c_create_count,
        'c_start_count': c_start_count,
        'c_stop_count': c_stop_count,
        'c_restart_count': c_restart_count,
        'c_remove_count': c_remove_count,
        'c_running_count': c_running_count,
        'c_stopped_count': c_stopped_count,
        'c_paused_count': c_paused_count,
    }
    return render(request, 'home/index.html', context)


def index_user(request):
    if request.user.is_superuser:
        return redirect('home:index')
    user = request.user.username
    nodes = HostNode.objects.filter(users__username=user)
    return render(request, 'home/index_user.html', {'nodes': nodes})


def forbiden(request):
    return render(request, 'home/forbiden.html')
