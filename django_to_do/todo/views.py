from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import TaskForms
from .models import Tasks

# Create your views here.


def home(request):
    tasks =Tasks.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def create(request):
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =TaskForms()
    
    return render(request, 'create.html', {'form': form})
        