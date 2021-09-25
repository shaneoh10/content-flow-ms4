from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="cat_images/")
    followers = models.ManyToManyField(User, related_name="category_followers",
                                       blank=True)

    def follower_count(self):
        return self.followers.count()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="post_images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
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
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    comment_date = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name="comment_likes",
                                   blank=True)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
