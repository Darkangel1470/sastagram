from django.shortcuts import render,redirect
from signup.models import User
from django.db import IntegrityError


# Create your views here.
context = {
    'isSignup': True,
    'mode':'Registration'
}
def index(request):
    if request.method == 'POST': 
        print('posted')
        fname = request.POST.get('fname')
        uname = request.POST.get('uname')
        num = request.POST.get('phone')
        password = request.POST.get('pass')
        usr = User(fname=fname, uname=uname, number=num, password=password)
        try:
            usr.save()
            request.session['uname'] = uname
            print(request.session['uname']," signned up")
            return redirect('/')
        except IntegrityError as e:
            context = {
                'isSignup': True,
                'mode':'Registration',
                'message': e.__cause__,
            }
            print("Duplicate value"+str(e.__cause__))
            return render(request, 'signup/signup.html', context)
    context = {
        'isSignup': True,
        'mode':'Registration'
    }  
    return render(request, 'signup/signup.html', context)

def user_register(request):
    return render(request, 'signup/signup.html')
