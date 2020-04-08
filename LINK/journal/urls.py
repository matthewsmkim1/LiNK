from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='journal-home'),
    path('about/', views.about, name='journal-about'),
]
