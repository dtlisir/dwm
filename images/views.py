from django.shortcuts import render, redirect
from django.http import JsonResponse
from hosts.models import HostNode
from common.utils import handle_size, handle_time
from common.docker_api import get_images

def image_list(request, pk):
    if request.user.is_superuser:
        node = HostNode.objects.get(id=pk)
    else:
        user = request.user.username
        check_node = HostNode.objects.filter(id=pk, users__username=user)
        if not check_node:
            return redirect('home:forbiden')
        node = check_node[0]
    return render(request, 'images/image_list.html', {'node': node})


def get_image_list(request):
    try:
        url = request.POST.get('node_url')
        resp_data = []
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
        return JsonResponse({'data': resp_data})
    except Exception as e:
        return JsonResponse({'data': []})

