# Generated by Django 2.2.16 on 2022-08-29 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_titlecategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TitleCategory',
        ),
    ]