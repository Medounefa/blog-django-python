from telnetlib import AUTHENTICATION
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

# Create your views here.

def SignIn(request):
    print("logggggg")
    if request.method == "POST" :
        form = LoginForm(request.POST  or None)
        if form.is_valid():
            print("form valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(username=username, password=password)
            print("use ",user)
            if user is not None:
                login(request, user)
                return redirect("/")
        else :
            print("errors ",form.errors)
    else :
        form = LoginForm()
    return render(request, "utilisateurs/signIn.html", {"form":form})

def register_user(request) :
     if request.method == "POST":
         
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password = raw_password )
            return redirect("/login/")
            #  password2 = form.cleaned_data.get("password2")
            # email = form.cleaned_data.get("email")
     
     else:
        form = SignUpForm()
     return render(request, "utilisateurs/signUp.html", {"form":form})
 
 
def profile(request) :
        
        user = request.user
        return render(request, "utilisateurs/profil.html", {"user":    user })
 
# def profile(request, username, email) :
#         profil = get_object_or_404(register_user, username=username, email=email)
#         return render(request, "utilisateurs/profil.html", {"pro":    profil })