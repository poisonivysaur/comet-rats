from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import *
from .models import *

# Create your views here.
def homeURL(request):
    return redirect('home')

def home(request):
    return render(request, 'rats/home.html')

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('login')

    else:
        form = UserForm()
    return render(request,'registration/register.html',{'UserForm' : form})

def attendance(request):
    return render(request, 'rats/home.html')

def residency(request):
    return render(request, 'rats/home.html')

def projects(request):
    return render(request, 'rats/home.html')

def teams(request):
    return render(request, 'rats/home.html')
