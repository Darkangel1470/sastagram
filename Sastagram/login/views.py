from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def index(request):
    context = {
        'mode': 'Login',
        'isLogin': False
    }
    return render(request, "login/login.html", context)