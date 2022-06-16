from django.urls import path
from .views import index, about
from django.urls import path, include
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
