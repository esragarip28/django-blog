from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()            
            messages.success(request,'Kayıt işlemi Başarıyla Gerçekleştirildi...')
            return render(request,"index.html")

    form=RegisterForm()
    return render(request,"register.html",{"form":form})




def loginUser(request):
   
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.warnings(request,"Lütfen tekrar giriş bilgilerinizi yazınız...")
            return render(request,"login.html",context)

        messages.success(request,"başarılı giriş işlemi....")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context) 







