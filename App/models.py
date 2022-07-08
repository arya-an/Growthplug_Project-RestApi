from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
#from rest_framework.authtoken.models import Token

# Create your models here.

GENRE_CHOICE=(
    ('Fantasy','Fantasy'),
    ('Literary','Literary'),
    ('Mystery','Mystery'),
    ('Non-Fiction','Non-Fiction'),
    ('Science Fiction','Science Fiction'),
    ('Thriller','Thriller'),
)

STAR_CHOICE=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)


class Ebook(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50,choices=GENRE_CHOICE)
    review = models.IntegerField(choices=STAR_CHOICE)
    favorite = models.BooleanField(default=False)
    def __str__(self):
        return self.title


# @receiver(post_save, sender =settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)
   