# Generated by Django 5.0 on 2023-12-08 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_season', to='course_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='coursevideo',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='season', to='course_app.season'),
        ),
    ]