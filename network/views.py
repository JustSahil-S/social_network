import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from .models import User, Post
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.generic import ListView

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    print (paginator.count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print (page_obj)
    try: 
        User.objects.get(username=request.user.username)
        return render(request, "network/index.html", {
        "page_obj": page_obj,
        "user": User.objects.get(username=request.user.username)
    })
    except: 
        return render(request, "network/index.html", {
        "posts": page_obj,
    })
def follow_page(request):
    users = User.objects.all().filter(followers = request.user)
    posts = Post.objects.all().filter(poster__in = users)
    paginator = Paginator(posts, 5)
    print (paginator.count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print (page_obj)
    try: 
        User.objects.get(username=request.user.username)
        return render(request, "network/index.html", {
        "page_obj": page_obj,
        "user": User.objects.get(username=request.user.username)
    })
    except: 
        return render(request, "network/index.html", {
        "posts": page_obj,
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def posts(request):
    if request.method == "POST":
        content = request.POST["post"]
        user = User.objects.get(username=request.user.username)
        post = Post.objects.create(poster=user, content=content, dateTime=datetime.now(),)
        post.save()
        return HttpResponseRedirect(reverse("index"))

def profile(request, user):
    
    following = User.objects.all().filter(followers = User.objects.get(username=user))
    count = following.count()
    print(count)
    posts = Post.objects.all().filter(poster=User.objects.get(username=user))
    paginator = Paginator(posts, 5)
    print (paginator.count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print (page_obj)
    return render(request, "network/profile.html", {
        "user": User.objects.get(username=user),
        "page_obj": page_obj,
        "count": count
    })

def likePosts(request, id):
    post = Post.objects.get(id=id)
    print(f'LIKES: {post.likes.all()}')
    if request.user not in post.likes.all(): 
        post.likes.add(User.objects.get(username=request.user.username))
        likeCount = post.likes.all().count()
        likeCount = {"likecount": likeCount}
        print(likeCount)
    else:
        post.likes.remove(User.objects.get(username=request.user.username))
        likeCount = post.likes.all().count()
        likeCount = {"likecount": likeCount}
        print(likeCount)
    if request.method == "GET":
        return JsonResponse(likeCount)
    
@csrf_exempt
def edit(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post.objects.get(id=id)
        print(data)
        print(post)
        post.content = data["newContent"]
        post.save()
        return HttpResponse(status=204)

def follow(request, user):
    login_user = request.user
    login_username = login_user.username
    if user != login_username:
        user = User.objects.get(username=user)
        if login_user not in user.followers.all(): 
            user.followers.add(login_user)
            followCount = user.followers.all().count()
            followCount = {"followcount": followCount}
            print(followCount)
        else:
            user.followers.remove(login_user)
            followCount = user.followers.all().count()
            followCount = {"followcount": followCount}
            print(followCount)
        if request.method == "GET":
            return JsonResponse(followCount)
