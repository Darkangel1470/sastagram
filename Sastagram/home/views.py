from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # try:
        print(request.session['uname']," opened home page")
        context = {
            'uname': request.session['uname']
        }
        return render(request, 'home/home.html',context)
    # except:
        # print("redirected to login from home")
        # return redirect("login/")

def logout(request):
    try:
        del request.session['uname']
        return redirect("../login/")
    except KeyError as e:
        print(e.__cause__)
        return redirect("../login/")