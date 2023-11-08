from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


class Post(models.Model):

    user = models.ForeignKey(User,on_delete=models.PROTECT)
    likes_count = models.IntegerField()
    comments_count = models.IntegerField()
    liked = models.BooleanField(default=False)


class PostLikes(models.Model):

    post = models.ForeignKey(Post,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT)


class PostComments(models.Model):

    post = models.ForeignKey(Post,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    comment = models.CharField(max_length=200)


