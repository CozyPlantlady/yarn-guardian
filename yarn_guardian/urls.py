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
from stash import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),

    path('', views.home, name='home'),

    path('get_stash', views.get_stash, name='get_stash'),
    path('add_yarn', views.add_yarn, name='add_yarn'),
    path('edit_yarn/<yarn_id>', views.edit_yarn, name='edit_yarn'),
    path('delete_yarn/<yarn_id>', views.delete_yarn, name='delete_yarn'),

    path('get_projects', views.get_projects, name='get_projects'),
    path('add_project', views.add_project, name='add_project'),
    path('edit_project/<project_id>', views.edit_project, name='edit_project'),
    path('delete_project/<project_id>',
         views.delete_project, name='delete_project'),
]
