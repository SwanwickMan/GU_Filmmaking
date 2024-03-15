from django.db import models
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    #added these MAX_LENGTH things for form.py and i think it counts as clean code
    CATEGORY_MAX_LENGTH=128
    name = models.CharField(max_length=CATEGORY_MAX_LENGTH, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    MOVIE_MAX_LENGTH=200
    title = models.CharField(max_length=MOVIE_MAX_LENGTH)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos_uploaded', validators=
    [FileExtensionValidator(allowed_extensions=['mp4'])]) #ensures only mp4 video is uploaded
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Poster(models.Model):
    POSTER_MAX_LENGTH=200
    title = models.CharField(max_length=POSTER_MAX_LENGTH)
    image = models.ImageField(upload_to='posters/', validators=
    [FileExtensionValidator(allowed_extensions=['png', 'jpg'])]) #ensures only png & jpg image is uploaded
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return f"Poster {self.id}"

class BehindTheScene(models.Model):
    BTS_MAX_LENGTH=200
    title = models.CharField(max_length=BTS_MAX_LENGTH)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    file = models.FileField(upload_to='file_path')
    likes = models.IntegerField(default=0)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        if extension in ['mp4', 'mpg', 'mpeg']:
            return 'video'
        if extension in ['jpg', 'jpeg', 'png']:
            return 'image'
    
    def __str__(self):
        return self.description