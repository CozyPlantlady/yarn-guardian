from . import views
from django.urls import path

urlpatterns = [
    path('', views.GetStash.as_view(), name='home')
]

