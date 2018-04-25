from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    """ USER MODEL """


    GENDER_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified'),
    }

    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True, blank=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    #followers, following에 blank=True를 해주면 가입할시에 follower, followers가 필수가 아니게 된다. 궁금하면 실험해보길.
    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()