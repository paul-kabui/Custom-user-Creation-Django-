from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    context = {}
    return render(request,"login.html",context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        telephone = request.POST.get("tel")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        
        if username != "":
            if len(telephone) > 14:
                pass
            else:
                if not email:
                    pass
                else:
                    if len(password) <= 5 and len(password1) <=5:
                        pass
                    else:
                        if password == password1:
                            print("success")
                
    return redirect("login")

def login_url(request):
    if request.method == "POST":
        #email= request.POST.get("email")
        print("incoming data")
    return HttpResponse("data recieved")

def signup_view(request):
    context = {}
    return render(request,"signup.html",context)