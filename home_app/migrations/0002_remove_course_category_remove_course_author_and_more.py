# Generated by Django 5.0 on 2023-12-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
