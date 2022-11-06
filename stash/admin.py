from django.contrib import admin
from .models import Producer, Yarn, Material, ColorGroup, Weight, Amount, Project
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Producer, Yarn, Material, ColorGroup, Weight, Amount, Project)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
    search_fields = ['name']
