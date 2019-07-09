from django.shortcuts import render
from django.http import JsonResponse
from hosts.models import HostNode
from common.utils import handle_size, handle_time
from common.docker_api import get_images

def image_list(request):
    nodes = HostNode.objects.values('id', 'name')
    return render(request, 'images/image_list.html', {'nodes': nodes})


def get_image_list(request):
    node_id = request.GET.get('node_id')
    resp_data = []
    try:
        node = HostNode.objects.get(id=node_id)
        url = node.url
        resp = get_images(url)
        if resp['result']:
            for data in resp['data']:
                i_data = {
                    'short_id': data.short_id,
                    'tag': data.tags[0],
                    'size': handle_size(data.attrs['Size']),
                    'created': handle_time(data.attrs['Created'][:-11]),
                    'i_id': data.id,
                }
                resp_data.append(i_data)
    except Exception as e:
        pass
    return JsonResponse({'data': resp_data})


