from user_auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "user_profile")
    pincode = models.IntegerField(blank=False,null= False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


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


#test model to check use of serializer in graphql

class Employee(models.Model):

    name = models.CharField(max_length=40)
    salary = models.IntegerField()

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name