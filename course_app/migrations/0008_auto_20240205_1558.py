# Generated by Django 3.1.4 on 2024-02-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0007_auto_20240205_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='course_app.course'),
        ),
    ]
