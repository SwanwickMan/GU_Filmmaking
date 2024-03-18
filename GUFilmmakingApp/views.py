from django.shortcuts import render
from GUFilmmakingApp.forms import PostForm, PosterForm, MovieForm, BTSForm
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from GUFilmmakingApp.models import Category, Post, UserProfile


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-views')[:3]
    context_dict = {}
    context_dict['category'] = category_list
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'home.html', context=context_dict)
    return response


def search(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'GUFilmmakingApp/search.html')


def profile(request):
    context_dict = {}
    response = render(request, 'GUFilmmakingApp/profile.html', context=context_dict)

    return response


def user_liked(request):
    context_dict = {}
    response = render(request, 'user_liked.html', context=context_dict)

    return response


def user_posts(request):
    context_dict = {}
    response = render(request, 'user_posts.html', context=context_dict)

    return response


def categories(request):
    context_dict = {}
    response = render(request, 'categories.html', context=context_dict)

    return response


# implement slugs later
def long_movies(request, content_name_slug):
    context_dict = {}
    response = render(request, 'GUFilmmakingApp/content_page.html', context=context_dict)

    return response


def short_movies(request, content_name_slug):
    context_dict = {}
    response = render(request, 'GUFilmmakingApp/short_movies.html', context=context_dict)

    return response


def add_movie(request):

    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('GUFilmmakingApp:home'))
        else:
            print(form.errors)
    
    return render(request, 'add_movie.html', {'form': form})


def posters(request, content_name_slug):
    context_dict = {}
    response = render(request, 'GUFilmmakingApp/posters.html', context=context_dict)

    return response


def add_poster(request):

    form = PosterForm()

    if request.method == 'POST':
        form = PosterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('GUFilmmakingApp:posters'))
        else:
            print(form.errors)
    
    return render(request, 'add_poster.html', {'form': form})


def behind_the_scenes(request):
    context_dict = {}

    posts = Post.objects.filter(post_type="bts")
    context_dict['posts'] = posts

    response = render(request, 'GUFilmmakingApp/behind_the_scenes.html', context=context_dict)

    return response


def add_bts(request):

    form = BTSForm()

    if request.method == 'POST':
        form = BTSForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('GUFilmmakingApp:behind_the_scenes'))
        else:
            print(form.errors)
    
    return render(request, 'add_bts.html', {'form': form})

def add_post(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(user=request.user)
            post.author_id = UserProfile.objects.get(user=request.user).userID
            post.category = Category.objects.get(name=request.POST.get('category'))
            post.views = 0
            post.likes = 0
            post.save()
            return redirect(reverse('GUFilmmakingApp:index'))
        else:
            print(form.errors)
    
    return render(request, 'GUFilmmakingApp/add_post.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('GUFilmmakingApp:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'GUFilmmakingApp/login.html')


def user_signup(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'GUFilmmakingApp/signup.html')


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
        request.session['visits'] = visits


