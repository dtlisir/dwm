from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_networks


def network_list(request):
    nodes = HostNode.objects.values('id', 'name')
    return render(request, 'networks/network_list.html', {'nodes': nodes})


def get_network_list(request):
    node_id = int(request.GET.get('node_id'))

    resp_data = []
    try:
        node = HostNode.objects.get(id=node_id)
        url = node.url
        resp = get_networks(url)
        if resp['result']:
            for data in resp['data']:
                v_data = {
                    'short_id': data.short_id,
                    'scope': data.attrs['Scope'],
                    'driver': data.attrs['Driver'],
                    'subnet': data.attrs['IPAM']['Config'][0]['Subnet'] if data.attrs['IPAM']['Config'] else '',
                    'gateway': data.attrs['IPAM']['Config'][0]['Gateway'] if data.attrs['IPAM']['Config'] else '',
                    'created': data.attrs['Created'][:-16],
                }
                resp_data.append(v_data)
    except Exception as e:
        pass
    return JsonResponse({'data': resp_data})
