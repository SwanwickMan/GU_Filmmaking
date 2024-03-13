from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    video = models.FileField(upload_to='videos_uploaded')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Poster(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posters/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)


    def __str__(self):
        return f"Poster {self.id}"

class BehindTheScene(models.Model):
    title = models.CharField(max_length=200)
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