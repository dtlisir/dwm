from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_volumes

def volume_list(request):
    nodes = HostNode.objects.values('id', 'name')
    return render(request, 'volumes/volume_list.html', {'nodes': nodes})


def get_volume_list(request):
    node_id = int(request.GET.get('node_id'))

    resp_data = []
    try:
        node = HostNode.objects.get(id=node_id)
        url = node.url
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
    except Exception as e:
        pass
    return JsonResponse({'data': resp_data})



