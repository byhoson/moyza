from django.shortcuts import render
from django.http import HttpResponse
from .models import Lightning, Comment, Catcher
from django.views import generic
from .forms import LightningForm
from django.shortcuts import redirect


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:      
            all_lightnings = Lightning.objects.all()
            num_visits = request.session.get('num_visits', 0)
            request.session['num_visits'] = num_visits + 1
            return render(request, 'cloud.html', context={'all_lightnings':all_lightnings, 'num_visits':num_visits})
        else:
            return HttpResponse('hello')


def test_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'registration/login.html')
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


def lightning_new(request):
    if request.method == "POST":
        form = LightningForm(request.POST)
        if form.is_valid():
            lightning = form.save(commit=False)
            lightning.created_by = request.user
            #lightning.created_at = timezone.now()
            lightning.save()
            return redirect('lightning', pk=lightning.pk)
    else:
        form = LightningForm()
    return render(request, 'throw.html', {'form': form})
