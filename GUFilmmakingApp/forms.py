from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from GUFilmmakingApp.models import Category, Movie, Post, Poster, BehindTheScene

CAT_YEAR_CHOICES = (
    ("a", "2022-23"),
    ("b", "2023-24")
)

CAT_MOVIE_CHOICES = (
    ("a", "Longer 2022-23"),
    ("b", "Longer 2023-24"),
    ("c", "Shorter 2022-23"),
    ("d", "Shorter 2023-24")
)


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=Movie.MOVIE_MAX_LENGTH,
                            help_text="Please enter the movie's title.")
    description = forms.CharField()
    video = forms.FileField(validators=
    [FileExtensionValidator(allowed_extensions=['mp4'])], help_text="Please enter an mp4 video.")
    category = forms.ChoiceField(choices=CAT_MOVIE_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # left slug in comment idk what part will be slugged
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # associate the form with the Movie model
        model = Movie
        fields = ('title', 'description', 'video', 'category')


class PosterForm(forms.ModelForm):
    title = forms.CharField(max_length=Poster.POSTER_MAX_LENGTH,
                            help_text="Please enter the poster's title.")
    description = forms.CharField()
    image = forms.ImageField(validators=
    [FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
                             help_text="Please upload a png or jpg image file.")
    category = forms.ChoiceField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # associate the form with the Poster model
        model = Poster
        fields = ('title', 'description', 'image', 'category')


class BTSForm(forms.ModelForm):
    title = forms.CharField(max_length=BehindTheScene.BTS_MAX_LENGTH,
                            help_text="Please enter the title.")
    description = forms.CharField()
    category = forms.ChoiceField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    file = forms.FileField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = BehindTheScene
        fields = ('title', 'description', 'file', 'category')

class PostForm(forms.ModelForm):

    CAT_CHOICES = (
        ("2023-24", "2023-24"),
        ("2022-23", "2022-23"),
        ("Longer Movies", "Longer Movies"),
        ("Shorter Movies", "Shorter Movies"),
    )

    year = forms.CharField(max_length=7, help_text="Please enter the year")
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    #file = forms.FileField()
    category = forms.ChoiceField(choices=CAT_CHOICES, help_text="category")
    title = forms.CharField(max_length=200, help_text="Please enter title")
    description = forms.CharField(help_text="Please enter the description")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Post
        fields = ('year', 'post_type', 'file', 'title', 'description',)
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
