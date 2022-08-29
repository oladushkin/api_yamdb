# Generated by Django 2.2.16 on 2022-08-29 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220828_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Category')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Title')),
            ],
        ),
    ]
