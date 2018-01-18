from django.shortcuts import render
from django.http import HttpResponse
from .models import Lightning, Comment, Catcher
from django.views import generic


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:      
            all_lightnings = Lightning.objects.all()
            return render(request, 'cloud.html', context={'all_lightnings':all_lightnings})
        else:
            return HttpResponse('hello')


def profile_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            my_lightning = Lightning.objects.get(created_by__username=request.user.username)
            
            return render(request, 'profile.html', context={'my_lightning': my_lightning})
        else:
            return HttpResponse('hello')


def lightning_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            
            return render(request, 'lightning.html', context={'my_lightning': my_lightning})
        else:
            return HttpResponse('hello')


class LightningListView(generic.ListView):
    model = Lightning
    context_object_name = 'all_lightnings'
    template_name = 'cloud.html'


class LightningDetailView(generic.DetailView):
    model = Lightning

    template_name = 'lightning.html'


