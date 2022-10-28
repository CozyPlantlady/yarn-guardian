from django.contrib import admin
from .models import Producer, Yarn
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Producer, Yarn)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
    search_fields = ['name']


