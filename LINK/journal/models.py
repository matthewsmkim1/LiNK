from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
import os
from groups.models import LinkGroup
from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='NULL', upload_to='profile_pics')
    video = models.FileField(default='NULL', upload_to="profile_pics")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group_to_post = models.ForeignKey(LinkGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
