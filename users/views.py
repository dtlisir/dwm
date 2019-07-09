from django.shortcuts import render
from django.http import JsonResponse
from blueapps.account.models import User
from django.shortcuts import render

def login_list(request):
    return render(request, 'users/login_list.html')


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


def user_detail(request):
    username = request.user.username
    user = User.objects.get(username=username)
    return render(request, 'users/user_detail', {'user': user})

def ops_list(request):
    return render(request, 'users/ops_list.html')
