from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            password=password,
            name="True",
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):

    username = None
    email = models.EmailField(verbose_name='email address', unique=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):              # __unicode__ on Python 2
        return self.email
