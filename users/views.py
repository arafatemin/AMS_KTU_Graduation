from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm, ProfileForm




@login_required
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'Authentication/register.html', {
                    "error": "bu ad kullaniliyor.",
                    "username": username,
                    "email": email,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'Authentication/register.html', {
                        "error": "bu email kullaniliyor.",
                        "username": username,
                        "email": email,
                    })
                else:
                    user = User.objects.create_user(username=username, last_name=lastname, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'Authentication/register.html', {
                "error": "Parola eslesmiyor.",
                "username": username,
                "emial": email,
            })

    return render(request, "Authentication/register.html")

@login_required
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "Authentication/login.html", {
                "error": "username veya parola yanlis"
            })
    else:
        return render(request, "Authentication/login.html")



@login_required
def logout_view(request):
    logout(request)
    return redirect("login")




@login_required
def profile_view(request):
    return render(request, "Authentication/profile.html")


@login_required
def setting_view(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Basarili bir sekilde degisiklik yapabildiniz")
            return redirect("profile")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, "Authentication/setting.html", context)


