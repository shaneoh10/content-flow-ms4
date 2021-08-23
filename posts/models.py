from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    comment_date = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name="comment_likes",
                                   blank=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
