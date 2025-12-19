from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('quiz/', quiz, name='quiz'),
    path('dashboard/', dashboard, name='dashboard'),
    path('result/', result, name='result'),
    path('base/', base, name='base'),
    path('login/', login_html, name='login'),
    path('login-enter/', login_page, name='login-enter'),
    path('profile/', setting, name='setting'),
    path('logout/', logout_page, name="logout"),
]