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
    path('', views.base, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('most_liked/', views.most_liked, name='most_liked'),
    path('most_viewed/', views.most_viewed, name='most_viewed'),
    path('profile/', views.profile, name='profile'),
    path('categories/', views.categories, name='categories'),
    path('categories/behind_the_scenes/', views.behind_the_scenes, name='behind_the_scenes'),
    path('categories/behind_the_scenes/videos/', views.videos, name='videos'),
    path('categories/behind_the_scenes/photos/', views.photos, name='photos'),
    path('categories/movies/', views.movies, name='movies'),
    path('categories/movies/shorter_movies/', views.short_movies, name='shorter_movies'),
    path('categories/movies/shorter_movies/2022_23/', views.sm_2022_23, name='sm_2022_23'),
    path('categories/movies/shorter_movies/2023_24/', views.sm_2023_24, name='sm_2023_24'),
    path('categories/movies/longer_movies/', views.long_movies, name='longer_movies'),
    path('categories/movies/longer_movies/2022_23/', views.lm_2022_23, name='lm_2022_23'),
    path('categories/movies/longer_movies/2023_24/', views.lm_2023_24, name='lm_2023_24'),
    path('categories/posters/', views.posters, name='posters'),
    path('categories/posters/2022_23/', views.p_2022_23, name='p_2022_23'),
    path('categories/posters/2023_24/', views.p_2023_24, name='p_2023_24'),

]