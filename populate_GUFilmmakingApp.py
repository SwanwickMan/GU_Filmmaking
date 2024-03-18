import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GU_Filmmaking.settings')
import django
django.setup()
from GU_Filmmaking import settings
from django.contrib.auth.models import User
from GUFilmmakingApp.models import Category, Post, UserProfile


def populate(author):

    movies_longer_2022_23 = [
        {'title' : 'Circa 2008', 'filepath' : settings.MEDIA_DIR + '/circa2008Movie.mp4', 'description' : 'Suspense & Thriller'}
    ]

    movies_shorter_2022_23 = [
        {'title' : 'FourPlay', 'filepath' : settings.MEDIA_DIR + '/FourPlayMovie.mp4', 'description' : 'Romance'}
    ]

    movies_longer_2023_24 = [
        {'title' : 'Jamie Learns the Sellotape Technique', 'filepath' : settings.MEDIA_DIR + '/jamieLearnsTheSellotapeTechniqueMovie.mp4', 'description' : 'Comedy'}
    ]

    movies_shorter_2023_24 = [
        {'title' : 'Do You Believe In Santa Claus?', 'filepath' : settings.MEDIA_DIR + '/SantaFilm.mp4', 'description' : 'Satire & Comedy'}
    ]

    posters_2022_23 = [
        {'title' : 'Circa 2008 Poster', 'filepath' : settings.MEDIA_DIR + '/poster2022-2023.jpg', 'description' : 'Our beautiful poster'},
        {'title' : 'FourPlay Poster', 'filepath' : settings.MEDIA_DIR + '/FourPlayPoster.jpg', 'description': 'cool kids poster!'}
    ]

    posters_2023_24 = [
        {'title' : 'Fortune Cookie', 'filepath' : settings.MEDIA_DIR + '/poster2023-2024.jpg', 'description': 'so proud of this beautiful poster!'},
        {'title' : 'Do You Believe In Santa Claus? Poster', 'filepath' : settings.MEDIA_DIR + '/BYBISCposter.jpg', 'description': 'Cool Movie Poster'}
    ]

    behind_the_scenes_2022_23 = [
        {'title' : "tiktok1", 'filepath' : settings.MEDIA_DIR + '/bts.mp4', 'description' : 'Our First TikTok!', 'description': 'A day on set'},
        {'title' : 'FourPlay Party Photos', 'filepath' : settings.MEDIA_DIR + '/FourPlayBTS.jpg', 'description' : 'BTS Party Scene Fourplay 2023'}
    ]

    behind_the_scenes_2023_24 = [
        {'title' : 'tiktok2', 'filepath' : settings.MEDIA_DIR + '/guFilmTiktok.mp4', 'description' : 'Our Second TikTok!', 'description': 'behind the scenes on our shoots'},
        {'title' : 'Santa Claus Shoot Photos', 'filepath' : settings.MEDIA_DIR + '/bts.jpg', 'description' : 'BTS on DYBISC 2024 first shoot'}
    ]

    movie_cats = {'Longer Movies': {'2022-23': {'movies': movies_longer_2022_23}, '2023-24': {'movies': movies_shorter_2022_23}},
              'Shorter Movies': {'2022-23': {'movies': movies_longer_2023_24}, '2023-24': {'movies': movies_shorter_2023_24}}
    }

    poster_cats = {'2022-23' : {'posters' :posters_2022_23},
                   '2023-24' : {'posters' : posters_2023_24 }
    }

    behind_the_scenes_cats = {'2022-23' : {'bts' :behind_the_scenes_2022_23},
                   '2023-24' : {'bts' : behind_the_scenes_2023_24 }
    }

    users = [
        {'username': 'User1', 'email':'example1@filmmaking.com', 'password': 'password1', 'userID': '00001', 'filepath': '/profile1.jpg', 'bio': 'Example Bio User1'},
        {'username': 'User2', 'email':'example2@filmmaking.com', 'password': 'password2', 'userID': '00002', 'filepath': '/profile2.jpg', 'bio': 'Example Bio User2'},
        {'username': 'User3', 'email':'example3@filmmaking.com', 'password': 'password3', 'userID': '00003', 'filepath': '/profile3.jpg', 'bio': 'Example Bio User3'},
        {'username': 'User4', 'email':'example4@filmmaking.com', 'password': 'password4', 'userID': '00004', 'filepath': '/profile4.jpg', 'bio': 'Example Bio User4'},
        {'username': 'User5', 'email':'example5@filmmaking.com', 'password': 'password5', 'userID': '00005', 'filepath': '/profile5.jpg', 'bio': 'Example Bio User5'}
    ]

    
    for cat, cat_data in movie_cats.items():
        for year, movies_data in cat_data.items():
            c = add_cat(cat)
            for m in movies_data['movies']:
                add_post(c, m['title'], m['filepath'], m['description'], year, author)
    
    for cat, cat_data in poster_cats.items():
        c = add_cat(cat)
        for p in cat_data['posters']:
            add_post(c, p['title'], p['filepath'], p['description'], year, author)
    
    for cat, cat_data in behind_the_scenes_cats.items():
        c = add_cat(cat)
        for b in cat_data['bts']:
            add_post(c, b['title'], b['filepath'], b['description'], year, author)

    for user_data in users:
        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'])
        user_profile = UserProfile.objects.create(user=user, userID=user_data['userID'], profileImage=settings.MEDIA_DIR + user_data['filepath'], bio=user_data['bio'])
        user_profile.save()

   
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_post(cat, title, media, description, year, author, views=0, likes=0 ):
    print("Adding post with author:", author)
    p = Post.objects.get_or_create(category=cat, title=title, author=author)[0]
    p.description = description
    p.year = year
    p.views = random.randint(0,100)
    p.likes = random.randint(0,100)
    p.post_type()
    p.file = media
    p.save()
    return p


if __name__ == '__main__':
    print('Starting population script...')
    user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
    user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', verified=True, bio='Example User Bio')
    populate(author=user_profile)