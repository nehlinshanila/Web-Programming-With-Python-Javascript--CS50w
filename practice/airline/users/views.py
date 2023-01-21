from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
        return render(request, "users/user.html")

def login_views(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["username"]
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials"
            })
    return render(request, "users/login.html")

def logout_views(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged Out"
    })
    pass