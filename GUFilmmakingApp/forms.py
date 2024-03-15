from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from GUFilmmakingApp.models import Movie, Poster, BehindTheScene

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
    video = forms.FileField(upload_to='videos_uploaded', validators=
    [FileExtensionValidator(allowed_extensions=['mp4'])], help_text="Please enter an mp4 video.")
    category = forms.CharField(choices=CAT_MOVIE_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #left slug in comment idk what part will be slugged
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        #associate the form with the Movie model
        model = Movie
        fields = ('title, description, video, category')

class PosterForm(forms.ModelForm):
    title = forms.CharField(max_length=Poster.POSTER_MAX_LENGTH,
    help_text="Please enter the poster's title.")
    image = forms.ImageField(upload_to='posters/', validators=
    [FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
    help_text="Please upload a png or jpg image file.")
    category = forms.CharField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        #associate the form with the Poster model
        model = Poster
        fields = ('title, description, image, category')

class BTSForm(forms.ModelForm):
    title = forms.CharField(max_length=BehindTheScene.BTS_MAX_LENGTH,
    help_text="Please enter the title.")
    description = forms.CharField()
    category = forms.CharField(choices=CAT_YEAR_CHOICES, help_text="Please select the year.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    file = forms.FileField(upload_to='file_path')
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = BehindTheScene
        fields = ('title, description, file, category')