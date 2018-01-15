from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            
            return render(request, 'index.html')
        else:
            return HttpResponse('hello')

