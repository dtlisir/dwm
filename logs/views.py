from django.shortcuts import render

from django.shortcuts import render

def login_list(request):
    return render(request, 'logs/loginlist.html')


def ops_list(request):
    return render(request, 'logs/ops_list.html')
