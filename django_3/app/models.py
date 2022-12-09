from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=350)
    category = models.CharField(max_length=50)
    blog_id = models.CharField(max_length=50)
    blog_by_author = models.CharField(max_length=50)
    # blog_by_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"
