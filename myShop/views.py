from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q

from .models import *


# Create your views here.
def index(request):
    content = {
        'title': 'Home',
        'sliderData': Slider.objects.all().order_by('-id')
    }
    return render(request, 'pages/home.html', content)


def store(request, slug):
    content = {
        'title': 'Store',
        'submenuData': SubMenu.objects.prefetch_related('items_set').filter(slug=slug)
    }
    return render(request, 'pages/store.html', content)


def item_details(request, slug):
    content = {
        'title': 'Item-details',
        'itemData': Items.objects.filter(slug=slug)
    }
    return render(request, 'pages/item_details.html', content)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail('Hi this is ' + name, message, email, ['nmkcktm@gmail.com'])
        messages.success(request, "Message sent successfully")
        return redirect('contact')
    else:
        content = {
            'title': 'Contact'
        }
        return render(request, 'pages/contact.html', content)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, 'Error loging in')
            return redirect('login')
    else:
        content = {
            'title': 'Login',
            'form': AuthenticationForm
        }
    return render(request, 'pages/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('register')
        else:
            messages.error(request, 'User not registered')
            return redirect('register')
    else:
        content = {
            'title': 'Register',
            'form': UserCreationForm
        }
    return render(request, 'pages/register.html', content)


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')


@login_required(login_url='login')
def users(request):
    content = {
        'title': 'User'
    }
    return render(request, 'pages/Users.html', content)


def search_results(request):
    if request.method == 'POST':
        search = request.POST['search']
        item_list = Items.objects.filter(Q(item_name__icontains=search) or Q(sub_menu__icontains=search))
    content = {
        'title': 'Search-results',
        'items_list': item_list
    }
    return render(request, 'pages/search_results.html', content)
