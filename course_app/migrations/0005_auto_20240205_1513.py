# Generated by Django 3.1.4 on 2024-02-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_auto_20240205_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='created_at',
        ),
        migrations.AddField(
            model_name='season',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_app.course'),
        ),
    ]