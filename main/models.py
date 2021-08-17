from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Channel(models.Model):
    Category = models.ManyToManyField(Category)
    Channel_name = models.CharField(max_length=100)
    Channel_image = models.ImageField()

    def __str__(self):
        return self.Channel_name


class Program(models.Model):
    Channel = models.ForeignKey(Channel, on_delete=models.RESTRICT)
    Program_name = models.CharField(max_length=200)
    Program_time = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.Program_name
