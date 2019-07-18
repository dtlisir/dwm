# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_networks


def network_list(request, pk):
    if request.user.is_superuser:
        node = HostNode.objects.get(id=pk)
    else:
        user = request.user.username
        check_node = HostNode.objects.filter(id=pk, users__username=user)
        if not check_node:
            return redirect('home:forbiden')
        node = check_node[0]
    return render(request, 'networks/network_list.html', {'node': node})


def get_network_list(request):
    try:
        resp_data = []
        url = request.POST.get('node_url')
        resp = get_networks(url)
        if resp['result']:
            for data in resp['data']:
                subnet = ''
                if data.attrs['IPAM']['Config']:
                    subnet = data.attrs['IPAM']['Config'][0]['Subnet']
                v_data = {
                    'short_id': data.short_id,
                    'scope': data.attrs['Scope'],
                    'driver': data.attrs['Driver'],
                    'subnet': subnet,
                    'created': data.attrs['Created'][:-16],
                }
                resp_data.append(v_data)
        return JsonResponse({'data': resp_data})
    except Exception as e:
        return JsonResponse({'data': []})

