from django.db import models

from users.models import Profile
from journal.models import Post
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth.models import Group
from django.contrib.auth.hashers import BCryptSHA256PasswordHasher as bcrypt
# Create your models here.


#! TODO add some functionality so that we can have multuple groups with the same name, but different bkey
#! right now when adding someone to the group they need to present the bkey, since django cannot filter based on binaryfield I hacked in
#! it filtering based on the group_name --> this means can only have unique group names for now
class LinkGroup(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    group_description = models.CharField(max_length=2000, default="New Group!")
    date_created = models.DateTimeField(default=timezone.now)
    members = models.ManyToManyField(Profile)
    posts = models.ManyToManyField(Post)
    bkey = models.BinaryField()  # this must be hashed using bycrpt to a b"" string
    # todo add calendar and announcments to a group
    # calender =
    # announcments =

    def __str__(self):
        return f"{self.group_name} {self.group_description}"

    # def get_absolute_url(self):
    #     return reverse('group-detail', kwargs={'pk': self.pk})
