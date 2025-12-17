from django.urls import path
from .views import quiz, dashboard, index, result, base, login, setting

urlpatterns = [
    path('', index, name='index'),
    path('quiz/', quiz, name='quiz'),
    path('dashboard/', dashboard, name='dashboard'),
    path('result/', result, name='result'),
    path('base/', base, name='base'),
    path('login/', login, name='login'),
    path('profile/', setting, name='setting'),
]