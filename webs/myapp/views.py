from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserForm


# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = CustomUserForm()
    return render(request, 'myapp/register.html', {'form': form})
