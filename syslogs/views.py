from django.shortcuts import render
from django.http import JsonResponse
from blueapps.account.models import User
from django.shortcuts import render

def user_list(request):
    return render(request, 'syslogs/user_list.html')


def get_user_list(request):
    users = User.objects.all()
    data = []
    for user in users:
        user_dict = {
            'name': user.username,
            'role': '管理员' if user.is_superuser else '普通用户',
            'nickname': user.nickname,
            'last_login': user.last_login.strftime("%Y-%m-%d %H:%M:%S"),
            'date_joined': user.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(user_dict)
    return JsonResponse({'data': data})

def ops_list(request):
    return render(request, 'syslogs/ops_list.html')
