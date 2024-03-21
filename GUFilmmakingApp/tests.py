from django.test import TestCase, Client, RequestFactory
from GUFilmmakingApp.models import *
from GUFilmmakingApp.views import *
from django.contrib.auth.models import User
from GU_Filmmaking import settings
from django.urls import reverse
from GUFilmmakingApp.models import Post

# Create your tests here.

def movie_set_up():
        user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
        user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', 
                                                  verified=True, bio='Example User Bio')

        movie = Post.objects.get_or_create(author=user_profile)[0]
        movie.title = "my movie"
        movie.post_type = "longer_movie"
        movie.description = "description"
        movie.thumbnail = settings.MEDIA_DIR + '/profilePhoto.jpg'
        movie.file = settings.MEDIA_DIR + '/FourPlayMovie.mp4'
        movie.save()
        return movie

class PostMethodTests(TestCase):
    
    def test_Post_views_and_likes_positive(self):
        user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
        user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg', verified=True, bio='Example User Bio')
        tester = Post.objects.get_or_create(title='test', author=user_profile)[0]
        tester.views = -1
        tester.likes = -1
        tester.year = "2023-24"
        tester.post_type = "Longer Movie"
        tester.save()
        self.assertEqual((tester.views>=0), True)
        self.assertEqual((tester.likes>=0), True)

class BtsViewTests(TestCase):
    def test_redirect_bts_posts(self):
        request = self.client.get('behind_the_scenes')
        response = behind_the_scenes(request, 'false-slug')
        response.client = Client()

        self.assertRedirects(response, '/GUFilmmakingApp/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

class MoviesViewTests(TestCase):
    def test_display_movie_post(self):
        movie = movie_set_up()
        #request = self.client.get('categories/movies/my-movie')
        url = reverse('GUFilmmakingApp:movies', kwargs={'content_name_slug':movie.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "my movie")
        

class SearchViewTests(TestCase):
    def test_no_posts(self):
        number_of_posts = len(Post.objects.all())

        url = reverse('GUFilmmakingApp:search') + '?search='

        # Make a GET request to the URL
        response = self.client.get(url)

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if 'search_results' is present in the context dictionary
        self.assertIn('search_results', response.context)

        # Get the search results from the context dictionary
        search_results = response.context['search_results']

        # Assert the number of search results
        self.assertEqual(len(search_results), number_of_posts)

    def test_search_post(self):
        movie = movie_set_up()

        url = reverse('GUFilmmakingApp:search') + '?search=my&search_for=longer_movie'
        response = self.client.get(url)
        self.assertIn('search_results', response.context)
        search_results = response.context['search_results']
        result = search_results.values()
        self.assertEqual(result[0]["title"], "my movie")

class ProfileViewTests(TestCase):
    def test_profile(self):
        user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
        user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg',
                                                   verified=True, bio='Example User Bio')
        self.client.login(username="filmmaking_populate_user", password="example_password123")

        url = reverse("GUFilmmakingApp:profile", kwargs={"content_name_slug" : user_profile.slug})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "filmmaking_populate_user")

    