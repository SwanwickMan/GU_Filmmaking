from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from GUFilmmakingApp.models import Post, UserProfile

POST_TYPE_CHOICES = (
        ('longer_movie', 'Longer Movie'),
        ('shorter_movie', 'Shorter Movie'),
    )


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the movie's title.")
    description = forms.CharField(help_text="Please enter a description.")
    file = forms.FileField(required=True, help_text="Please enter an mp4 video.", )
    thumbnail = forms.ImageField(required=True, help_text="Optional: Upload a thumbnail image")
    post_type = forms.ChoiceField(choices=POST_TYPE_CHOICES, widget=forms.RadioSelect, initial='longer_movie', help_text="Please select movie type")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # associate the form with the Movie model
        model = Post
        fields = ('title', 'description', 'file', 'thumbnail', 'post_type')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Extract user from kwargs
        super(MovieForm, self).__init__(*args, **kwargs)


class PosterForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the poster's title.")
    description = forms.CharField(help_text="Please enter a description.")
    file = forms.FileField(required = True, validators=
                             [FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
                             help_text="Please upload a png or jpg image file.")
    thumbnail = forms.ImageField(required=False, help_text="Optional: Upload a thumbnail image")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='poster') 

    class Meta:
        # associate the form with the Poster model
        model = Post
        fields = ('title', 'description', 'file', 'post_type', 'thumbnail')


class BTSForm(forms.ModelForm):
    title = forms.CharField(max_length=Post.POST_MAX_LENGTH,
                            help_text="Please enter the title.")
    description = forms.CharField(help_text="Please enter a description.")
    thumbnail = forms.ImageField(required=False, help_text="Optional: Upload a thumbnail image")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    file = forms.FileField(required=True, help_text="Please upload a file")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    post_type = forms.CharField(widget=forms.HiddenInput(), initial='bts')

    class Meta:
        model = Post
        fields = ('title', 'description', 'file', 'post_type', 'thumbnail')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profileImage',)
        help_texts = {
            'profileImage': "Accepted: png, jpg."
        }
        widgets = {
            'profileImage': forms.FileInput(attrs={'accept': 'image/png, image/jpeg'})
        }


class BioForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio',)
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        
