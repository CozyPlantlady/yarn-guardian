from django.contrib import admin
from .models import Producer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Producer)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')
    search_fields = ['name']
