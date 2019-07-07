from django.shortcuts import render

def image_list(request):
    return render(request, 'images/image_list.html')