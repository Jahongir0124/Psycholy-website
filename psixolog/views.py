from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.models import Group, Permission,User
from .decorator import *
from .models import *
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    data = Psychologist.objects.all()
    project = Projects.objects.all()
    return render(request,'index.html',{'data':data,'proekt':project})
# @allowed_users(roles=['Psixolog'])
def add_user(request):
    form = UserForm(request.POST)
    psixolog = Psychologist()
    if request.method == 'POST':
        if form.is_valid():
            psixolog.user = User.objects.create_user(username=form.data['username'], email=form.data['email'], password=form.data['password1'])
            psixolog.name = form.cleaned_data['name']
            psixolog.phone_number = form.cleaned_data['phone_number']
            psixolog.save()
            return redirect('/')
        else:
            return HttpResponse('saqlamadi')
    return render(request,'add_user.html',{'form':form})

def group_view(request):
    group = Group.objects.all()
    return HttpResponse('salom')

def register_view(request):
    form = RegisterForm(request.POST)
    # name = Register()
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
            user.save()
            return redirect('/login')
    except Exception as e:
        return render(request,'register.html',{'alr':'yes'})
    return render(request,'register.html',{'reg':form})

def start_test(request):
    return HttpResponse('<h1>Test boshlandi brat</h1>')
def read_article(request):
    article = Projects.objects.all()
    return render(request,'read_article.html',{'art':article})



