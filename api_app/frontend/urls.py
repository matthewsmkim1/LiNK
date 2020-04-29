from django.urls import path

from .views import index, PostDetailView

urlpatterns = [
    path('', index),
    path('login', index),
    path('register', index),
    path('create-post', index)
    #! for updating or deleting a post
    path('edit/<int:pk>', PostDetailView.as_view()),
    path('delete/<int:pk>', PostDetailView.as_view()),
]
