from django.urls import path

from .views import index, PostDetailView

urlpatterns = [
    path('', index),
    path('login', index),
    path('register', index),
    path('create-post', index),
    #! for updating or deleting a post
    path('edit/<int:pk>', PostDetailView.as_view()),
    path('delete/<int:pk>', PostDetailView.as_view()),
    #! for testing components
    path('new', index),
    path('view-group', index),
    path('group-entries', index),
    path('create-post', index),
    path('create-group', index),
    path('join-group', index),
    path('dashy', index),
]
