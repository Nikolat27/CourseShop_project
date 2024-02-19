from django.contrib import admin
from . import models


# Register your models here.


class VideoAdmin(admin.TabularInline):
    model = models.Lesson


class RequirementAdmin(admin.TabularInline):
    model = models.Requirements


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [RequirementAdmin]


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [VideoAdmin]
    autocomplete_fields = ['course']


admin.site.register(models.Category)
