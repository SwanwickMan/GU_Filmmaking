import os
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

    behind_the_scenes_vids = [
        {'title' : "tiktok1", 'filepath' : settings.MEDIA_DIR + '/bts.mp4', 'description' : 'Our First TikTok!', 'description': 'A day on set'},
        {'title' : 'tiktok2', 'filepath' : settings.MEDIA_DIR + '/guFilmTiktok.mp4', 'description' : 'Our Second TikTok!', 'description': 'behind the scenes on our shoots'}
    ]

    behind_the_scenes_pics = [
        {'title' : 'FourPlay Party Photos', 'filepath' : settings.MEDIA_DIR + '/FourPlayBTS.jpg', 'description' : 'BTS Party Scene Fourplay 2023'},
        {'title' : 'Santa Claus Shoot Photos', 'filepath' : settings.MEDIA_DIR + '/bts.jpg', 'description' : 'BTS on DYBISC 2024 first shoot'}
    ]

    movie_cats = {'Longer Movies': {'2022-23': {'movies': movies_longer_2022_23}, '2023-24': {'movies': movies_shorter_2022_23}},
              'Shorter Movies': {'2022-23': {'movies': movies_longer_2023_24}, '2023-24': {'movies': movies_shorter_2023_24}}
    }

    poster_cats = {'2022-23' : {'posters' :posters_2022_23},
                   '2023-24' : {'posters' : posters_2023_24 }
    }

    behind_the_scenes_cats = {'videos' : {'bts' :behind_the_scenes_vids},
                   'pictures' : {'bts' : behind_the_scenes_pics }
    }

    
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

   
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_post(cat, title, media, description, year, author, views=0, likes=0 ):
    print("Adding post with author:", author)
    p = Post.objects.get_or_create(category=cat, title=title, author=author)[0]
    p.description = description
    p.year = year
    p.views = views
    p.likes = likes
    p.file = media
    p.save()
    return p

if __name__ == '__main__':
    print('Starting population script...')
    user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
    user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', verified=True, bio='Example User Bio')
    populate(author=user_profile)