# Generated by Django 4.0.3 on 2022-03-14 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]
