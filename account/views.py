from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from articles.models import *

def home(request):
    articles = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'account/home.html', {'articles': articles})

def signupuser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'account/signupuser.html', {'error': 'Такой пользователь уже существует'})
                except ValueError:
                    return render(request, 'account/signupuser.html', {'error': 'Неправильно введены данные'})
            else:
                return render(request, 'account/signupuser.html', {'error': 'Пароли не совпадают'})
        return render(request, 'account/signupuser.html')
    else:
        return redirect("home")

def loginuser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'account/loginuser.html', {'error': 'Неправильный логин или пароль'})
        return render(request, 'account/loginuser.html')
    else:
        return redirect("home")

def logoutuser(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")
