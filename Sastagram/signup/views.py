from django.shortcuts import render
from signup.models import User

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
        usr.save()
        print(str(usr.id))

    return render(request, 'signup/signup.html', context)

def user_register(request):
    return render(request, 'signup/signup.html')
