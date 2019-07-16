from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_networks


def network_list(request, pk):
    node = HostNode.objects.get(id=pk)
    return render(request, 'networks/network_list.html', {'node': node})


def get_network_list(request):
    try:
        resp_data = []
        url = request.POST.get('node_url')
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
        return JsonResponse({'data': resp_data})
    except Exception as e:
        return JsonResponse({'data': []})

