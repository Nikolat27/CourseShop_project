from django.contrib import admin
from . import models


# Register your models here.


class VideoAdmin(admin.TabularInline):
    model = models.Lesson


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [VideoAdmin]
    autocomplete_fields = ['course']


admin.site.register(models.Category)
