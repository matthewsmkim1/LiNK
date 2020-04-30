# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='NULL', upload_to='profile_pics')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " By " + self.author

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
