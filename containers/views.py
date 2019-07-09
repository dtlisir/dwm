from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import HostNode
from common.docker_api import get_containers
from common.utils import timestamp_to_datetime

def container_list(request):
    nodes = HostNode.objects.values('id', 'name')
    return render(request, 'containers/container_list.html', {'nodes': nodes})

def get_container_list(request):
    node_id = request.GET.get('node_id')
    resp_data = []
    try:
        node = HostNode.objects.get(id=node_id)
        url = node.url
        resp = get_containers(url)
        if resp['result']:
            for data in resp['data']:
                c_data = {
                    'c_id': data.id,
                    'name': data.name,
                    'image': data.image.attrs['RepoTags'][0] if data.image.attrs['RepoTags'] else '',
                    'created': data.attrs.get('Created',''),
                    'status': data.status,
                }
                resp_data.append(c_data)
    except Exception as e:
        pass
    return JsonResponse({'data': resp_data})


def container_create(request):
    return render(request, 'containers/container_create.html')