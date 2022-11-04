"""yarn_guardian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stash.views import home, get_stash, add_yarn, edit_yarn, delete_yarn, projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stash/', get_stash, name='get_stash'),
    path('add_yarn', add_yarn, name='add_yarn'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('edit/<yarn_id>', edit_yarn, name='edit_yarn'),
    path('delete/<yarn_id>', delete_yarn, name='delete_yarn'),
    path('projects', projects, name='projects'),
]
