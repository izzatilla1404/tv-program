from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.utils.translation import get_language


class Category(models.Model):
    category_uz = models.CharField(max_length=50)
    category_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.category_uz

    @property
    def category(self):
        return getattr(self, 'category_{}'.format(get_language()))


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
