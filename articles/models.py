from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now())
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
