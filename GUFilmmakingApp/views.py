from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {}
    response = render(request, 'base.html', context=context_dict)

    return response


def search(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'signup.html')


def profile(request):
    context_dict = {}
    response = render(request, 'profile.html', context=context_dict)

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
    response = render(request, 'content_page.html', context=context_dict)

    return response


def short_movies(request, content_name_slug):
    context_dict = {}
    response = render(request, 'short_movies.html', context=context_dict)

    return response


def posters(request, content_name_slug):
    context_dict = {}
    response = render(request, 'posters.html', context=context_dict)

    return response


def behind_the_scenes(request, content_name_slug):
    context_dict = {}
    response = render(request, 'behind_the_scenes.html', context=context_dict)

    return response


def user_login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'signup.html')





