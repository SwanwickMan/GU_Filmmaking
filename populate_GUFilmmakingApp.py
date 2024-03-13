import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'GU_Filmmaking.settings')
import django
django.setup()
from GU_Filmmaking import settings
from GUFilmmakingApp.models import Category, Movie, Poster, BehindTheScene


def populate():

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
        {'title' : 'Circa 2008 Poster', 'filepath' : settings.MEDIA_DIR + '/poster2022-2023.jpg'},
        {'title' : 'FourPlay Poster', 'filepath' : settings.MEDIA_DIR + '/FourPlayPoster.jpg'}
    ]

    posters_2023_24 = [
        {'title' : 'Fortune Cookie', 'filepath' : settings.MEDIA_DIR + '/poster2023-2024.jpg'},
        {'title' : 'Do You Believe In Santa Claus? Poster', 'filepath' : settings.MEDIA_DIR + '/BYBISCposter.jpg'}
    ]

    behind_the_scenes_vids = [
        {'title' : "tiktok1", 'filepath' : settings.MEDIA_DIR + '/bts.mp4', 'description' : 'Our First TikTok!'},
        {'title' : 'tiktok2', 'filepath' : settings.MEDIA_DIR + '/guFilmTiktok.mp4', 'description' : 'Our Second TikTok!'}
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
        c = add_cat(cat)
        for year, movies_data in cat_data.items():
            for m in movies_data['movies']:
                add_movie(c, m['title'], m['filepath'], m['description'])
    
    for cat, cat_data in poster_cats.items():
        c = add_cat(cat)
        for p in cat_data['posters']:
            add_poster(c, p['title'], p['filepath'])
    
    for cat, cat_data in behind_the_scenes_cats.items():
        c = add_cat(cat)
        for b in cat_data['bts']:
            add_bts(c, b['title'], b['filepath'], b['description'])

   
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_movie(cat, title, media, description, views=0, likes=0):
    m = Movie.objects.get_or_create(category = cat, title = title)[0]
    m.video=media
    m.description=description
    m.views=views
    m.likes=likes
    m.save()
    return m

def add_poster(cat, title, media, views=0, likes=0):
    p = Poster.objects.get_or_create(category = cat, title = title)[0]
    p.image = media
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_bts(cat, title, media, description, views=0, likes=0):
    b = BehindTheScene.objects.get_or_create(category = cat, title = title)[0]
    b.file=media
    b.description=description
    b.views=views
    b.likes=likes
    b.save()
    return b

if __name__ == '__main__':
    print('Starting population script...')
    populate()