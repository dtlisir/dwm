from django.shortcuts import render

def volume_list(request):
    return render(request, 'volumes/volume_list.html')
