"""GU_Filmmaking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from GUFilmmakingApp import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "GUFilmmakingApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<slug:content_name_slug>/', views.profile, name='profile'),
    path('behind_the_scenes/', views.behind_the_scenes, name='behind_the_scenes'),
    path('movies/<slug:content_name_slug>/', views.movie, name='movies'),
    path('short_films/<slug:content_name_slug>/', views.movie, name='short_movies'),
    path('bts/<slug:content_name_slug>/', views.behind_the_scenes, name='behind_the_scenes'),
    path('posters/<slug:content_name_slug>/', views.poster, name='posters'),
    path('add_poster/', views.add_poster, name='add_poster'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('add_behind_the_scenes/', views.add_bts, name='add_behind_the_scenes'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_redirect/<slug:content_type_slug>/<slug:content_name_slug>', views.redirect_from_slug, name='redirect_from_slug'),
    path('user_redirect/<slug:user_name_slug>/', views.get_user_profile, name='redirect_to_user'),
    path('profile/<slug:content_name_slug>/upload_pic/', views.upload_profile_pic, name='upload_profile_pic'),
    path('profile/<slug:content_name_slug>/update_bio/', views.update_bio, name='update_bio'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('update_views/<int:post_id>/', views.update_views, name='update_views'),
]