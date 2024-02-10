from django.contrib import admin
from . import models


# Register your models here.


class VideoAdmin(admin.TabularInline):
    model = models.Lesson


@admin.register(models.Season)
class SeasonADmin(admin.ModelAdmin):
    inlines = [VideoAdmin]


admin.site.register(models.Course)
admin.site.register(models.Category)
