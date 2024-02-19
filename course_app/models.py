from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    category = models.ManyToManyField(Category, related_name="categories")
    image = models.ImageField(upload_to="img/course_images")
    price = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    buyers = models.ManyToManyField(User, related_name="user_course", null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.description[:40]}"


class Season(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="seasons", null=True, blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="lessons", null=True, blank=True)
    title = models.CharField(max_length=100)
    duration = models.FloatField(validators=[MinValueValidator(0.30), MaxValueValidator(30.00)])
    video = models.FileField(upload_to="vid/course_video")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Requirements(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="requirements", null=True, blank=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
