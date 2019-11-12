# Generated by Django 2.2.3 on 2019-10-24 07:12

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('status', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=120, unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='Slider')),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('status', models.BooleanField(default=0)),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myShop.Menu')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sub Menu',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('status', models.BooleanField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='menus')),
                ('description', ckeditor.fields.RichTextField()),
                ('price', models.IntegerField()),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myShop.SubMenu')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
    ]