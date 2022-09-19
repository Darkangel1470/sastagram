from django.shortcuts import render,redirect
import mysql.connector as sql
from signup.models import User
from django.contrib.auth.models import User as Usr


def authenticate(username=None):
        try:
            user = Usr.objects.get(username=username)
        except Usr.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = Usr(username=username)
            user.save()
        return user

# Create your views here.
def index(request):
    context = {
        'mode': 'Login',
        'isLogin': False
    }
    # to handle login
    if request.method == 'POST' or True:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pass')

        users = User.objects.all()
        for usr in users:
            print("%s == %s = %s"%(usr.uname, uname,usr.uname==uname))
            if usr.uname == uname:
                print("%s == %s = %s"%(usr.password, pwd,usr.password==pwd))
                if(usr.password==pwd):
                    request.session['uname'] = uname
                    print(request.session['uname']," logged in")
                    return redirect('/')
                else:
                    return render(request, 'login/login.html', {'alert':"Incorrect Password"})
            else:
                return render(request, 'login/login.html', {'alert':"Incorrect Username"})
    return render(request, "login/login.html", context)