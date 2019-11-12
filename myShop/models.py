from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name_plural = 'Menu'


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    status = models.BooleanField(default=0)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Menu'


class Items(models.Model):
    sub_menu = models.ForeignKey(SubMenu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(blank=True, upload_to='menus')
    description = RichTextField()
    price = models.IntegerField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = 'Items'


class Slider(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=120, unique=True)
    description = RichTextField()
    image = models.ImageField(blank=False, upload_to='Slider')
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.title
