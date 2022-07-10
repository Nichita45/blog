from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=255)   
    email = models.EmailField()
    address = models.CharField(max_length=100, default="")
    number = models.CharField(max_length=15, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    uploadedtime = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absoulte_url(self):
        return reverse('article_detail', kwargs={"slug": self.slug}) 

    def __str__(self):
        return self.name