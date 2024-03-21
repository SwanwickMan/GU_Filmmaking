from django.shortcuts import render
from django.db.models import Q
from GUFilmmakingApp.forms import PosterForm, MovieForm, BTSForm, UserForm, ProfilePicForm, BioForm
from django.shortcuts import redirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from GUFilmmakingApp.models import Post, UserProfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    most_liked_posts = Post.objects.all().order_by('-likes')[:3]
    most_viewed_posts = Post.objects.all().order_by('-views')[:3]
    context_dict = {
        'most_liked_posts': most_liked_posts,
        'most_viewed_posts': most_viewed_posts,
    }
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'GUFilmmakingApp/home.html', context=context_dict)
    return response


def search(request):
    search_term = request.GET.get('search', '')
    search_for = request.GET.get('search_for', 'All')
    sort_by = request.GET.get('sort_by', 'relevancy')
    print("searchTerms: ", search_term, search_for, sort_by)

    # begin to filter and sort search results
    if search_for == "Users":
        search_results = search_for_users(search_term)
        for result in search_results: print(result.user, "|", result.slug)
        context_dict = {"search_results": search_results, "type": "user"}
    else:
        search_results = search_for_posts(search_term, search_for, sort_by)
        for result in search_results: print(result.post_type, "|", result)
        context_dict = {"search_results": search_results, "type": "post"}

    return render(request, 'GUFilmmakingApp/search.html', context=context_dict)


def profile(request, content_name_slug):
    try:
        user_profile = UserProfile.objects.get(slug=content_name_slug)
        profile_posts = Post.objects.filter(author=user_profile)
        liked_posts = user_profile.myLikes.all()

    except UserProfile.DoesNotExist:
        return redirect("GUFilmmakingApp:index")
    
    profile_pic_form = ProfilePicForm(instance=user_profile)
    bio_form = BioForm(initial={'bio': user_profile.bio})

    context_dict = {"profile": user_profile,
                    "profile_pic_form": profile_pic_form,
                    "bio_form": bio_form,
                    "profile_posts": profile_posts,
                    "liked_posts": liked_posts,
                    }

    print(user_profile.myLikes.values())

    return render(request, 'GUFilmmakingApp/profile.html', context=context_dict)


def user_liked(request):
    context_dict = {}
    response = render(request, 'user_liked.html', context=context_dict)

    return response


def user_posts(request):
    context_dict = {}
    response = render(request, 'user_posts.html', context=context_dict)

    return response


@login_required
def add_movie(request):
    form = MovieForm()

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(user=request.user)
            post.save()
            return redirect(reverse('GUFilmmakingApp:index'))
        else:
            print(form.errors)

    return render(request, 'GUFilmmakingApp/add_movie.html', {'form': form})


def poster(request, content_name_slug):
    try:
        search_results = Post.objects.filter(post_type="poster")
        search_results = search_results.get(slug=content_name_slug)
    except Post.DoesNotExist:
        return redirect("GUFilmmakingApp:index")

    context_dict = {"poster": search_results}
    response = render(request, 'GUFilmmakingApp/poster.html', context=context_dict)

    return response


def movie(request, content_name_slug):
    try:
        search_results = Post.objects.filter(Q(post_type="longer_movie") | Q(post_type="shorter_movie"))
        search_results = search_results.get(slug=content_name_slug)
    except Post.DoesNotExist:
        return redirect("GUFilmmakingApp:index")

    context_dict = {"movie": search_results}
    response = render(request, 'GUFilmmakingApp/movie.html', context=context_dict)

    return response


def behind_the_scenes(request, content_name_slug):
    try:
        search_results = Post.objects.filter(post_type="bts")
        search_results = search_results.get(slug=content_name_slug)
    except Post.DoesNotExist:
        return redirect("GUFilmmakingApp:index")

    context_dict = {"bts": search_results, "file_type": get_file_extension(search_results)}

    response = render(request, 'GUFilmmakingApp/behind_the_scenes.html', context=context_dict)

    return response


@login_required
def add_poster(request):
    form = PosterForm()

    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(user=request.user)
            post.save()
            return redirect(reverse('GUFilmmakingApp:index'))
        else:
            print(form.errors)
    
    return render(request, 'GUFilmmakingApp/add_poster.html', {'form': form})


@login_required
def add_bts(request):
    form = BTSForm()

    if request.method == 'POST':
        form = BTSForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = UserProfile.objects.get(user=request.user)
            post.save()
            return redirect(reverse('GUFilmmakingApp:index'))
        else:
            print(form.errors)
    
    return render(request, 'GUFilmmakingApp/add_bts.html', {'form': form})


@login_required
def add_post(request):
    return render(request, 'GUFilmmakingApp/add_post.html')


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
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)  # Hashes the password
            user.save()

            # Create UserProfile
            UserProfile.objects.create(user=user, userID=user.id, profileImage='default.jpg', bio='')

            # Authenticate and login user after signup
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('GUFilmmakingApp:index')  # Redirect to a home page
    else:
        form = UserForm()
    return render(request, 'GUFilmmakingApp/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('GUFilmmakingApp:index')  # Redirect to the home page after logout


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


def update_likes(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'likes': post.likes})

@csrf_exempt
def update_views(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        post.views += 1
        post.save()
        return JsonResponse({'views': post.views})


# helper url to enable linking to site content more easily
def redirect_from_slug(request, content_type_slug, content_name_slug):
    if content_type_slug == "post":
        try:
            post = Post.objects.get(slug=content_name_slug)
        except Post.DoesNotExist:
            return redirect("GUFilmmakingApp:index")
        if post.post_type in ("longer_movie", "shorter_movie"):
            url = reverse('GUFilmmakingApp:movies', kwargs={'content_name_slug': content_name_slug})
        elif post.post_type == "poster":
            url = reverse('GUFilmmakingApp:posters', kwargs={'content_name_slug': content_name_slug})
        elif post.post_type == "bts":
            url = reverse('GUFilmmakingApp:behind_the_scenes', kwargs={'content_name_slug': content_name_slug})
        else:
            return redirect('GUFilmmakingApp:index')

        return redirect(url)
    elif content_type_slug == "profile":
        url = reverse('GUFilmmakingApp:profile', kwargs={'content_name_slug': content_name_slug})
        return redirect(url)
    else:
        return redirect('GUFilmmakingApp:index')


# another helper view to get user page
@login_required
def get_user_profile(request, user_name_slug):
    current_profile = UserProfile.objects.get(user__username=user_name_slug)
    url = reverse('GUFilmmakingApp:profile', kwargs={'content_name_slug': current_profile.slug})
    return redirect(url)


def get_file_extension(post):
    file_type = post.file.name.split(".")[-1]
    if file_type in ("jpg", "jpeg", "png"):
        return "image"
    elif file_type == "mp4":
        return "video"
    else:
        return "bad type"


def search_for_posts(search_term, search_for,sort_by):
    search_results = Post.objects.filter(title__icontains=search_term)
    if search_for != 'All':
        search_results = search_results.filter(post_type=search_for)
    if sort_by != 'relevancy':
        search_results = search_results.order_by(sort_by)
    return search_results


def search_for_users(search_term):
    return UserProfile.objects.filter(user__username__icontains=search_term)


def upload_profile_pic(request, content_name_slug):
    try:
        user_profile = UserProfile.objects.get(slug=content_name_slug)
    except UserProfile.DoesNotExist:
        return redirect("GUFilmmakingApp:index")
    
    if request.method == "POST":
        form = ProfilePicForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            profile_pic = form.cleaned_data['profileImage']
            profile = request.user.userprofile
            profile.profileImage = profile_pic
            profile.save()
            return redirect('GUFilmmakingApp:profile', content_name_slug=content_name_slug)  # Redirect to the profile page
        else:
            print(form.errors)
    else:
        form = ProfilePicForm()
    return render(request, 'profile.html', {'profile_pic_form': form})

def update_bio(request, content_name_slug):
    try:
        # Retrieve the user profile based on the slug
        user_profile = UserProfile.objects.get(slug=content_name_slug)
    except UserProfile.DoesNotExist:
        # Redirect to a suitable page if the profile does not exist
        return redirect("GUFilmmakingApp:index")

    if request.method == 'POST':
        form = BioForm(request.POST, instance=user_profile)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            profile = request.user.userprofile
            profile.bio = bio
            profile.save()
            return redirect('GUFilmmakingApp:profile', content_name_slug=content_name_slug)  # Redirect to the profile page
    else:
        form = BioForm(initial={'bio': request.user.userprofile.bio})
    return render(request, 'profile.html', {'bio_form': form})
