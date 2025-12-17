from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")

def base(request):
    return render(request, "base.html")

def login(request):
    return render(request, "login.html")

def quiz(request):
    return render(request, "quiz.html")

def result(request):
    return render(request, "result.html")

def setting(request):
    return render(request, "setting.html")