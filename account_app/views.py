from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("repassword")

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                return render(request, "account_app/register.html", context={"error": "Your Username is inValid"})
            else:
                User.objects.create_user(username=username, password=pass1)
                return redirect("account_app:login")
        else:
            return render(request, "account_app/register.html", context={"error": "Your Passwords Dont match"})
    return render(request, "account_app/register.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        login(request, user=user)
        return redirect("home_app:main")
    return render(request, "account_app/login.html")


def logout_user(request):
    logout(request)
    return redirect("account_app:login")


def about(request):
    return render(request, "account_app/about.html")
