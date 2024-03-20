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
        movie.post_type = "Longer Movie"
        movie.description = "description"
        movie.save()
        return movie

class PostMethodTests(TestCase):
    
    def test_Post_views_and_likes_positive(self):
        def add_cat(name):
            #c = Category.objects.get_or_create(name=name)[0]
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
    def test_redirect_bts_posts(self):
        request = self.client.get('behind_the_scenes')
        response = behind_the_scenes(request, 'false-slug')
        response.client = Client()

        self.assertRedirects(response, '/GUFilmmakingApp/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

class MoviesViewTests(TestCase):
    def test_redirect_movie_post(self):
        movie = movie_set_up()

        request = self.client.get('post_redirect/slug:<content_name_slug>')
        response = redirect_from_slug(request, movie.slug)
        response.client = Client()

        self.assertRedirects(response, '/GUFilmmakingApp/category/movies/my-movie/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_display_movie_post(self):
        movie = movie_set_up()
        print(Post.objects.get(slug=movie.slug))
        #request = self.client.get('categories/movies/my-movie')
        response = self.client.get(reverse('GUFilmmakingApp:movies', kwargs={'content_name_slug':movie.slug}))

        self.assertRedirects(response, '/GUFilmmakingApp/category/movies/my-movie/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'my movie')
        self.assertContains(response, 'description')
        

class SearchViewTests(TestCase):
    def test_no_posts(self):
        number_of_posts = len(Post.objects.all())
        print(number_of_posts)

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
class ProfileViewTests(TestCase):
    def test_profile(self):
        user = User.objects.create_user(username='filmmaking_populate_user', email='example@email.com',password='example_password123')
        user_profile = UserProfile.objects.create(user=user, userID=123, profileImage=settings.MEDIA_DIR + '/profilePhoto.jpg',
                                                   verified=True, bio='Example User Bio')
        self.client.login(username="filmmaking_populate_user", password="example_password123")

        response = self.client.get(reverse("GUFilmmakingApp:profile"))

        self.assertEqual(response.status_code, 200)