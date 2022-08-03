from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegisterForm,FeedbackForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("homePage")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request,"User not exists")
            return redirect('login')
        
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You are now logged in :) ")
            return  redirect("homePage")
        
        else:
            messages.error(request, "Username or password incorrect :( ")
            # return HttpResponse("Username or password incorrect")
            return redirect("login")


    return render(request,'users/login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,"Logout successfull :)")
    return redirect('login')


def registerUser(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request,user)
            messages.success(request,"Account was created successfully  :)")
            return redirect("homePage")
        else:
            messages.warning(request,"Error in your data ")
            return redirect("register")


    context = {'form':form}
    return render(request,'users/register.html',context)

@login_required(login_url='login')
def feedbackUser(request):
    user = request.user.username
    mail = request.user.email
    print(user,mail)
    form = FeedbackForm(user,mail)

    if request.method == "POST":
        form = FeedbackForm(user,mail, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"We got your response but we don't believe in democracy 😈")
            return redirect("homePage")
    context = {'form':form}
    return render(request,'users/feedback.html',context)
