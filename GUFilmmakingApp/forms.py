from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from GUFilmmakingApp.models import Category, Post

CAT_YEAR_CHOICES = [
    ("a", "2022-23"),
    ("b", "2023-24")
]

CAT_MOVIE_CHOICES = [
    ("a", "Longer 2022-23"),
    ("b", "Longer 2023-24"),
    ("c", "Shorter 2022-23"),
    ("d", "Shorter 2023-24")
]


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the movie's title.")
    description = forms.CharField(help_text="Please enter a description.")
    video = forms.FileField(validators=
    [FileExtensionValidator(allowed_extensions=['mp4'])], help_text="Please enter an mp4 video.")
    category = forms.ChoiceField(choices=CAT_MOVIE_CHOICES, help_text="Please select the year.")
    thumbnail = forms.ImageField(required=False, help_text="Optional: Upload a thumbnail image")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='movie')
    # left slug in comment idk what part will be slugged
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # associate the form with the Movie model
        model = Post
        fields = ('title', 'description', 'video', 'category', 'post_type', 'thumbnail')


class PosterForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the poster's title.")
    description = forms.CharField(help_text="Please enter a description.")
    image = forms.ImageField(validators=
    [FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
                             help_text="Please upload a png or jpg image file.")
    category = forms.ChoiceField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    thumbnail = image
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='poster') 


    class Meta:
        # associate the form with the Poster model
        model = Post
        fields = ('title', 'description', 'image', 'category', 'post_type', 'thumbnail')


class BTSForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the title.")
    description = forms.CharField(help_text="Please enter a description.")
    category = forms.ChoiceField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    thumbnail = forms.ImageField(required=False, help_text="Optional: Upload a thumbnail image")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    file = forms.FileField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='bts')
    class Meta:
        model = Post
        fields = ('title', 'description', 'file', 'category', 'post_type', 'thumbnail')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
