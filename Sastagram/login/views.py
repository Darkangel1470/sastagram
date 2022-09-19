from django.shortcuts import render
import mysql.connector as sql
from signup.models import User
# Create your views here.
def index(request):
    context = {
        'mode': 'Login',
        'isLogin': False
    }
            
    if request.method == 'POST' or True:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pass')
        users = User.objects.all()
        for user in users:
            print("%s == %s = %s"%(user.uname, uname,user.uname==uname))
            if user.uname == uname:
                print("%s == %s = %s"%(user.password, pwd,user.password==pwd))
                
                
    else:
        pass
    return render(request, "login/login.html", context)