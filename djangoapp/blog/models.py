from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog-post-image')
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    number_of_clicks = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
