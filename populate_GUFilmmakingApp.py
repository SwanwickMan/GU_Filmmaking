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
    categories = [add_cat(c) for c in ("2022-23", "2023-24")]

    movies_longer = [
        {'title': 'Circa 2008', 'filepath': settings.MEDIA_DIR + '/circa2008Movie.mp4', 'description' : 'Suspense & Thriller', "category": categories[0]},
        {'title': 'Jamie Learns the Sellotape Technique', 'filepath': settings.MEDIA_DIR + '/jamieLearnsTheSellotapeTechniqueMovie.mp4', 'description': 'Comedy', "category": categories[1]}

    ]

    shorter_movies = [
        {'title' : 'FourPlay', 'filepath' : settings.MEDIA_DIR + '/FourPlayMovie.mp4', 'description' : 'Romance',"category": categories[0]},
        {'title': 'Do You Believe In Santa Claus?', 'filepath': settings.MEDIA_DIR + '/SantaFilm.mp4','description': 'Satire & Comedy',"category": categories[1]}

    ]

    posters = [
        {'title' : 'Circa 2008 Poster', 'filepath' : settings.MEDIA_DIR + '/poster2022-2023.jpg', 'description' : 'Our beautiful poster',"category": categories[0]},
        {'title' : 'FourPlay Poster', 'filepath' : settings.MEDIA_DIR + '/FourPlayPoster.jpg', 'description': 'cool kids poster!',"category": categories[0]},
        {'title': 'Fortune Cookie', 'filepath': settings.MEDIA_DIR + '/poster2023-2024.jpg','description': 'so proud of this beautiful poster!',"category": categories[1]},
        {'title': 'Do You Believe In Santa Claus? Poster', 'filepath': settings.MEDIA_DIR + '/BYBISCposter.jpg','description': 'Cool Movie Poster',"category": categories[1]}
    ]

    behind_the_scenes = [
        {'title' : "tiktok1", 'filepath' : settings.MEDIA_DIR + '/bts.mp4', 'description' : 'Our First TikTok!', 'description': 'A day on set',"category": categories[0]},
        {'title' : 'FourPlay Party Photos', 'filepath' : settings.MEDIA_DIR + '/FourPlayBTS.jpg', 'description' : 'BTS Party Scene Fourplay 2023',"category": categories[0]},
        {'title': 'tiktok2', 'filepath': settings.MEDIA_DIR + '/guFilmTiktok.mp4', 'description': 'Our Second TikTok!', 'description': 'behind the scenes on our shoots',"category": categories[1]},
        {'title': 'Santa Claus Shoot Photos', 'filepath': settings.MEDIA_DIR + '/bts.jpg', 'description': 'BTS on DYBISC 2024 first shoot',"category": categories[1]}
    ]



    users = [
        {'username': 'User1', 'email':'example1@filmmaking.com', 'password': 'password1', 'userID': '00001', 'filepath': '/profile1.jpg', 'bio': 'Example Bio User1'},
        {'username': 'User2', 'email':'example2@filmmaking.com', 'password': 'password2', 'userID': '00002', 'filepath': '/profile2.jpg', 'bio': 'Example Bio User2'},
        {'username': 'User3', 'email':'example3@filmmaking.com', 'password': 'password3', 'userID': '00003', 'filepath': '/profile3.jpg', 'bio': 'Example Bio User3'},
        {'username': 'User4', 'email':'example4@filmmaking.com', 'password': 'password4', 'userID': '00004', 'filepath': '/profile4.jpg', 'bio': 'Example Bio User4'},
        {'username': 'User5', 'email':'example5@filmmaking.com', 'password': 'password5', 'userID': '00005', 'filepath': '/profile5.jpg', 'bio': 'Example Bio User5'}
    ]


    for data in movies_longer:
        add_post(data["category"], data['title'], data['filepath'], data['description'], "2023-24", author, "longer_movie")

    for data in shorter_movies:
        add_post(data["category"], data['title'], data['filepath'], data['description'], "2023-24", author, "shorter_movie")

    for data in posters:
        add_post(data["category"], data['title'], data['filepath'], data['description'], "2023-24", author, "poster")

    for data in behind_the_scenes:
        add_post(data["category"], data['title'], data['filepath'], data['description'], "2023-24", author, "bts")

    for user_data in users:
        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'])
        user_profile = UserProfile.objects.create(user=user, userID=user_data['userID'], profileImage=settings.MEDIA_DIR + user_data['filepath'], bio=user_data['bio'])
        user_profile.save()

   
def add_cat(name):
    print("Adding category ", name)
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_post(cat, title, media, description, year, author, post_type, views=0, likes=0):
    print("Adding post with author:", author)
    p = Post.objects.get_or_create(category=cat, title=title, author=author)[0]
    p.description = description
    p.year = year
    p.views = random.randint(0,100)
    p.likes = random.randint(0,100)
    p.post_type = post_type
    p.file = media
    p.save()
    return p


if __name__ == '__main__':
    print('Starting population script...')
    User.objects.all().delete()
    Category.objects.all().delete()
    Post.objects.all().delete()

    user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
    user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', verified=True, bio='Example User Bio')
    populate(author=user_profile)

    # temporary superuser
    User.objects.create_superuser('1', 'admin@example.com', '1')
