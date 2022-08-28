# Generated by Django 2.2.16 on 2022-08-28 17:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название жанра')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'verbose_name': 'Обзор',
                'verbose_name_plural': 'Обзоры',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название произведения')),
                ('year', models.PositiveSmallIntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(2022)], verbose_name='Год создания произведения')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(blank=True, related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Review')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('year',),
            },
        ),
        migrations.CreateModel(
            name='TitleGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Genre')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Title')),
            ],
        ),
    ]
