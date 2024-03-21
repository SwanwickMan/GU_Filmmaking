import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GU_Filmmaking.settings')
import django
django.setup()
from GU_Filmmaking import settings
from django.contrib.auth.models import User
from GUFilmmakingApp.models import Post, UserProfile


def populate(author):

    default_thumbnail = '/thumbnails/default_thumbnail.png'

    movies_longer = [
        {'title': 'Circa 2008', 'filepath': '/circa2008Movie.mp4', 'description' : 'Suspense & Thriller', 'thumbnail' : '/thumbnails/CircaPoster.jpg'},
        {'title': 'Jamie Learns the Sellotape Technique', 'filepath': '/jamieLearnsTheSellotapeTechniqueMovie.mp4', 'description': 'Comedy', 'thumbnail' : '/thumbnails/SellotapePoster.jpg'}

    ]

    shorter_movies = [
        {'title': 'FourPlay', 'filepath' : '/FourPlayMovie.mp4', 'description' : 'Romance', 'thumbnail' : '/thumbnails/fourPlay_thumbnail.jpg'},
        {'title': 'Do You Believe In Santa Claus?', 'filepath': '/SantaFilm.mp4','description': 'Satire & Comedy'}

    ]

    posters = [
        {'title': 'Circa 2008 Poster', 'filepath' : '/poster2022-2023.jpg', 'description' : 'Our beautiful poster'},
        {'title': 'FourPlay Poster', 'filepath' : '/FourPlayPoster.jpg', 'description': 'cool kids poster!'},
        {'title': 'Fortune Cookie', 'filepath': '/poster2023-2024.jpg','description': 'so proud of this beautiful poster!'},
        {'title': 'Do You Believe In Santa Claus? Poster', 'filepath': '/BYBISCposter.jpg','description': 'Cool Movie Poster'}
    ]

    behind_the_scenes = [
        {'title': "tiktok1", 'filepath' : '/bts.mp4', 'description' : 'Our First TikTok!', 'description': 'A day on set', 'thumbnail' : '/thumbnails/tiktok_thumbnail.jpg' },
        {'title': 'FourPlay Party Photos', 'filepath' : '/FourPlayBTS.jpg', 'description' : 'BTS Party Scene Fourplay 2023'},
        {'title': 'tiktok2', 'filepath': '/guFilmTiktok.mp4', 'description': 'Our Second TikTok!', 'description': 'behind the scenes on our shoots'},
        {'title': 'Santa Claus Shoot Photos', 'filepath': '/bts.jpg', 'description': 'BTS on DYBISC 2024 first shoot'}
    ]



    users = [
        {'username': 'User1', 'email':'example1@filmmaking.com', 'password': 'password1', 'userID': '00001', 'filepath': '/profile1.jpg', 'bio': 'Example Bio User1'},
        {'username': 'User2', 'email':'example2@filmmaking.com', 'password': 'password2', 'userID': '00002', 'filepath': '/profile2.jpg', 'bio': 'Example Bio User2'},
        {'username': 'User3', 'email':'example3@filmmaking.com', 'password': 'password3', 'userID': '00003', 'filepath': '/profile3.jpg', 'bio': 'Example Bio User3'},
        {'username': 'User4', 'email':'example4@filmmaking.com', 'password': 'password4', 'userID': '00004', 'filepath': '/profile4.jpg', 'bio': 'Example Bio User4'},
        {'username': 'User5', 'email':'example5@filmmaking.com', 'password': 'password5', 'userID': '00005', 'filepath': '/profile5.jpg', 'bio': 'Example Bio User5'}
    ]


    for data in movies_longer:
        add_post(data['title'], data['filepath'], data['description'], data.get("thumbnail", default_thumbnail),  author, "longer_movie")

    for data in shorter_movies:
        add_post(data['title'], data['filepath'], data['description'], data.get("thumbnail", default_thumbnail),  author, "shorter_movie")

    for data in posters:
        add_post(data['title'], data['filepath'], data['description'], data.get("thumbnail", default_thumbnail),  author, "poster")

    for data in behind_the_scenes:
        add_post(data['title'], data['filepath'], data['description'], data.get("thumbnail", default_thumbnail),  author, "bts")

    for user_data in users:
        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password'])
        user_profile = UserProfile.objects.create(user=user, userID=user_data['userID'], profileImage=user_data['filepath'], bio=user_data['bio'])
        user_profile.save()


def add_post(title, media, description, thumbnail, author, post_type, views=0, likes=0):
    print("Adding post with author:", author)
    p = Post.objects.get_or_create(title=title, author=author)[0]
    p.description = description
    p.thumbnail = thumbnail

    numArr = (random.randint(0, 100), random.randint(0, 100))
    p.views = max(numArr)
    p.likes = min(numArr)
    p.post_type = post_type
    p.file = media
    p.save()

    author.myLikes.add(p)

    return p


if __name__ == '__main__':
    print('Starting population script...')
    User.objects.all().delete()
    Post.objects.all().delete()

    user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
    user_profile = UserProfile.objects.create(user=user, userID=123, profileImage='/profilePhoto.jpg', verified=True, bio='Example User Bio')
    populate(author=user_profile)

    # temporary superuser
    User.objects.create_superuser('1', 'admin@example.com', '1')
