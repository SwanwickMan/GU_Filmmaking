import os
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path  

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4(), ext)
        return os.path.join(self.path, filename)
    

class Post(models.Model):
    POST_MAX_LENGTH = 200
    POST_TYPES = [
        ('shorter_movie', 'Shorter Movie'),
        ('longer_movie', 'Longer Movie'),
        ('poster', 'Poster'),
        ('bts', 'Behind the Scenes'),
    ]

    author = models.ForeignKey('GUFilmmakingApp.UserProfile', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    file = models.FileField(upload_to=PathAndRename('content'), null=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=PathAndRename('thumbnails'),
                                  validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                                  blank=True, null=False)
    views = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    likes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    def save(self, *args, **kwargs):
        if self.likes < 0:
            self.likes = 0
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.title)
        if self.file and not self.thumbnail:
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                self.thumbnail = self.file
            else:  # If thumbnail is not set
                self.thumbnail = 'thumbnails/default_thumbnail.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    userID = models.IntegerField()
    slug = models.SlugField(unique=True)
    profileImage = models.ImageField(default='/default_user_profile.jpg', upload_to="profileImage") #temp
    verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=200)
    myPosts = models.ForeignKey(Post, related_name='posted_by', on_delete=models.CASCADE, blank=True, null=True)
    myLikes = models.ManyToManyField(Post, related_name='liked_by', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    def is_admin(self):
        return self.user.is_staff
