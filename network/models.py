from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField('self', blank=True, default= None, null=True, symmetrical=False)

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length=500)
    dateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="postLikes", blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "poster": self.poster.username,
            "content": self.content,
            "dateTime": self.dateTime.strftime("%b %d %Y, %I:%M %p"),
            "likes": [user.username for user in self.likes.all()]
        }
