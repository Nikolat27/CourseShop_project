# Generated by Django 3.1.4 on 2024-02-05 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0008_auto_20240205_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
    ]
