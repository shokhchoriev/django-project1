from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "index.html")

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return redirect("login")

def base(request):
    return render(request, "base.html")

def login_html(request):
    return render(request, "login.html")

def login_page(request):
    if request.method =="POST":
        email = request.POST.get("email")
        parol = request.POST.get("password")
        user = authenticate(request, username=email, password=parol)
        if user is not None:
            login(request,user)
            return redirect("dashboard")

    return redirect ("login")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")

def quiz(request):
    return render(request, "quiz.html")

def result(request):
    return render(request, "result.html")

def setting(request):
    return render(request, "setting.html")