from django.shortcuts import render

def node_list(request):
    return render(request, 'hosts/node_list.html')


def add_node(request):
    return render(request, 'hosts/add_node.html')


def add_group(request):
    return render(request, 'hosts/add_group.html')