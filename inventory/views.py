from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# from .models import Profile,Post, Rating
# from .forms import PostForm, RatingsForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
import random

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')

def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'inv/index.html', context)


def display_desktops(request):
    items = Desktops.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'inv/index.html', context)


def display_mobiles(request):
    items = Mobiles.objects.all()
    context = {
        'items': items,
        'header': 'Mobiles',
    }
    return render(request, 'inv/index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_laptop(request):
    return add_item(request, LaptopForm)


def add_desktop(request):
    return add_item(request, DesktopForm)


def add_mobile(request):
    return add_item(request, MobileForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_laptop(request, pk):
    return edit_item(request, pk, Laptops, LaptopForm)


def edit_desktop(request, pk):
    return edit_item(request, pk, Desktops, DesktopForm)


def edit_mobile(request, pk):
    return edit_item(request, pk, Mobiles, MobileForm)


def delete_laptop(request, pk):

    template = 'inv/index.html'
    Laptops.objects.filter(id=pk).delete()

    items = Laptops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_desktop(request, pk):

    template = 'inv/index.html'
    Desktops.objects.filter(id=pk).delete()

    items = Desktops.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobile(request, pk):

    template = 'inv/index.html'
    Mobiles.objects.filter(id=pk).delete()

    items = Mobiles.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)



def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('/register')
        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1,
        ) 
        new_user.save() 
        return render (request,'login.html')
    return render(request,'register.html')

def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'userprofile.html', params)

# def profile(request):
#     user=request.user
#     my_profile=Profile.objects.get(user=user)
#     return render(request,"profile.html",{'my_profile':my_profile,"user":user})

def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")

# @login_required(login_url='/accounts/login/')
# def addpost(request):
#     if request.method=="POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post= form.save(commit=False)
#             post.user=request.user
#             post.save()
#             return redirect('/')

#     else:
#         form=PostForm()
#     try:
#         posts=Post.objects.all() 
#         posts=posts[::-1] 
#     except Post.DoesNotExist:
#         posts=None
#     return render(request,'newpost.html',{"form":form,"posts":posts}) 

# @login_required(login_url='/accounts/login/')
# def postproject(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user=request.user
#             project.save()
            
#         return redirect('/')
#     else:
#         form = PostForm()
#     try:
#         posts=Post.objects.all() 
#         posts=posts[::-1]
#         a_post = (0, len(posts)-1)
#         # random_post = posts[a_post]
#     except Post.DoesNotExist:
#         posts=None

#     context = {
#         'form':form,
#         # 'random_post': random_post
#     }
#     return render(request, 'newpost.html', context)


    


# @login_required(login_url='login')
# def update_profile(request):
    
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if user_form.is_valid() and prof_form.is_valid():
#             user_form.save()
#             prof_form.save()
#             # return HttpResponseRedirect(request.path_info)
#             return redirect('profile')

#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         prof_form = UpdateUserProfileForm(instance=request.user.profile)
#     contex = {
#         'user_form': user_form,
#         'prof_form': prof_form,

#     }
#     return render(request, 'update.html', contex)

