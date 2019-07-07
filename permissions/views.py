from django.shortcuts import render

from django.shortcuts import render

def permission_list(request):
    return render(request, 'permissions/permission_list.html')
