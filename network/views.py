from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
import json


from .models import User, Post


def index(request):
    posts = Post.objects.all().order_by("-timestamp")

    for post in posts:
        if request.user.is_authenticated:
            post.user_liked = request.user.liked.contains(post)
        else:
            post.user_liked = False

    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    context = {
        "posts": page
    }
    return render(request, "network/index.html", context)


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


# Create new post
@login_required
def new_post(request):
    if request.method == "POST":
        content = request.POST['content']
        author = request.user

        if content.strip() == '':
            messages.error(request, "Post cannot be empty!")

        else:
            messages.success(request, "Post created successfully.")
            post = Post(content=content, author=author)
            post.save()

        return redirect(reverse('index'))

    else:
        return render(request, 'network/index.html')


# A user's profile
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by("-timestamp")
    following_count = user.following.count()
    followers_count = user.followers.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    for post in page:
        if request.user.is_authenticated:
            post.user_liked = request.user.liked.contains(post)
        else:
            post.user_liked = False


    is_following = request.user.following.contains(user)

    context = {
        'posts': page,
        'user': user,
        'following_count': following_count,
        'followers_count': followers_count,
        'is_following': is_following
    }

    return render(request, 'network/profile.html', context)


@login_required
def follow(request, username):
    if request.method == 'POST':
        logged_in_user = request.user
        user_profile = get_object_or_404(User, username=username)

        if logged_in_user != user_profile:
            logged_in_user.following.add(user_profile)
        return redirect(reverse('profile', kwargs={'username': username}))

    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def unfollow(request, username):
    if request.method == 'POST':
        logged_in_user = request.user
        user_profile = get_object_or_404(User, username=username)

        if logged_in_user != user_profile:
            logged_in_user.following.remove(user_profile)
        return redirect(reverse('profile', kwargs={'username': username}))

    else:
        return HttpResponseNotAllowed(['POST'])



@login_required
def following(request):
    user_following = request.user.following.all()
    posts = Post.objects.filter(author__in=user_following).order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    for post in page:
        if request.user.is_authenticated:
            post.user_liked = request.user.liked.contains(post)
        else:
            post.user_liked = False


    return render(request, 'network/following.html', {"posts": page})


@login_required
def edit_post(request, post_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            content = data.get('content')
            post = get_object_or_404(Post, id=post_id)

            if request.user == post.author:
                if content:
                    if content.strip() == '':
                        return JsonResponse({'error': 'JSON is empty'}, status=400)

                    else:
                        post.content = content
                        post.save()
                        return JsonResponse({'status': 'success', 'updated_post': content})

            else:
                return HttpResponseForbidden("User is not allowed to edit this post!")

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)

        if request.user.liked.contains(post):
            request.user.liked.remove(post)
            return JsonResponse({'status': 'unliked', 'count': post.likes.count()})

        else:
            request.user.liked.add(post)
            return JsonResponse({'status': 'liked', 'count': post.likes.count()})


    else:
        return HttpResponseNotAllowed(['POST'])
