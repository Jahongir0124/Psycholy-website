from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import admin
a = []
def check_user(request):
    users = User.objects.filter(is_staff=True)
    for u in users:
        a.append(u.username)
    form = LoginForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
       login(request, user)
       if username in a:
           return redirect('/adminsite111')
       else:
            return redirect('/quiz')
    return render(request,'login_page.html',{'form':form})

def logout_view(request):
    logout(request)
    return check_user(request)

# def admin(request):
#     user = users.objects.get(category = 'admin')
#     if user:
#         return render(request, 'main/admin.html')
#
#     elif Exception:
#         return render(request, 'main/home.html')