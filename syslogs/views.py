from django.shortcuts import render
from django.http import JsonResponse
from syslogs.models import Log


def ops_list(request):
    return render(request, 'syslogs/ops_list.html')


def get_ops_list(request):
    if request.user.is_superuser:
        logs = Log.objects.all().order_by('-id')
    else:
        user = request.user.username
        logs = Log.objects.filter(user=user).order_by('-id')
    data = []
    if logs:
        data = [log.to_dict() for log in logs]
    return JsonResponse({'data': data})
