from django.contrib import admin
from .models import Yarn, Project
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Yarn, Project)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
    search_fields = ['name']
