# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_volumes

def volume_list(request, pk):
    if request.user.is_superuser:
        node = HostNode.objects.get(id=pk)
    else:
        user = request.user.username
        check_node = HostNode.objects.filter(id=pk, users__username=user)
        if not check_node:
            return redirect('home:forbiden')
        node = check_node[0]
    return render(request, 'volumes/volume_list.html',  {'node': node})


def get_volume_list(request):
    try:
        resp_data = []
        url = request.POST.get('node_url')
        resp = get_volumes(url)
        if resp['result']:
            for data in resp['data']:
                v_data = {
                    'short_id': data.short_id,
                    'driver': data.attrs['Driver'],
                    'mountpoint': data.attrs['Mountpoint'],
                    'created': data.attrs['CreatedAt'][:-6],
                    'v_id': data.id,
                }
                resp_data.append(v_data)
        return JsonResponse({'data': resp_data})
    except Exception as e:
        return JsonResponse({'data': []})


def volume_del(request):
    return JsonResponse({'data': []})

