from django.test import TestCase
from GUFilmmakingApp.models import Category, Post, UserProfile
from django.contrib.auth.models import User
from GU_Filmmaking import settings
from django.urls import reverse

# Create your tests here.

class PostMethodTests(TestCase):
    
    def test_Post_views_and_likes_positive(self):
        def add_cat(name):
            c = Category.objects.get_or_create(name=name)[0]
            c.save()
            return c
        
        categories = [add_cat(c) for c in ("2022-23", "2023-24")]
        user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
        user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', verified=True, bio='Example User Bio')
        tester = Post.objects.get_or_create(title='test', author=user_profile, category=categories[1])[0]
        tester.views = -1
        tester.likes = -1
        tester.year = "2023-24"
        tester.post_type = "Longer Movie"
        tester.save()
        self.assertEqual((tester.views>=0), True)
        self.assertEqual((tester.likes>=0), True)

class BtsViewTests(TestCase):
    def test_no_bts_posts(self):
        response = self.client.get(reverse('GUFilmmakingApp:behind_the_scenes'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no Behind The Scenes posts')
        self.assertQuerysetEqual(response.context['posts'], [])

class LongMoviesViewTests(TestCase):
    def test_no_long_movies_posts(self):
        response = self.client.get(reverse('GUFilmmakingApp:long_movies'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no Long Movies posts')
        self.assertQuerysetEqual(response.context['posts'], [])

class ShortMoviesViewTests(TestCase):
    def test_no_short_movies_posts(self):
        response = self.client.get(reverse('GUFilmmakingApp:short_movies'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no Short Movies posts')
        self.assertQuerysetEqual(response.context['posts'], [])

class PosterViewTests(TestCase):
    def test_no_posters_posts(self):
        response = self.client.get(reverse('GUFilmmakingApp:posters'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no Poster posts')
        self.assertQuerysetEqual(response.context['posts'], [])