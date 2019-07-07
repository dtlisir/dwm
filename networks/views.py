from django.shortcuts import render

def network_list(request):
    return render(request, 'networks/network_list.html')
