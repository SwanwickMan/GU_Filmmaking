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

app_name = "GUFilmmakingApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.categories, name='categories'),
    path('categories/behind_the_scenes/<slug:content_name_slug>/', views.behind_the_scenes, name='behind_the_scenes'),
    path('categories/movies/<slug:content_name_slug>/', views.long_movies, name='movies'),
    path('categories/shorts/<slug:content_name_slug>/', views.short_movies, name='short_movies'),
    path('categories/posters/<slug:content_name_slug>/', views.posters, name='posters'),
]