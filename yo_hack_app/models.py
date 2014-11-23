from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    image = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
        default='profile_pictures/default-profile-photo.png')
    api_token = models.CharField(max_length=100, null=True, blank=True)
    word1 = models.CharField(max_length=10, null=True, blank=True, default='dinner')
    word2 = models.CharField(max_length=10, null=True, blank=True)
    word3 = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u"{}".format(self.username)


class Family(models.Model):
    me = models.ForeignKey(Profile, related_name="families_me")
    you = models.ForeignKey(Profile, related_name="families_you")

    def __unicode__(self):
        return u"{}".format(self.you)


class Action(models.Model):
    HELLO = 0
    HELP = 1
    LOCATION = 2
    ACTIONS = (
        (HELLO, "hello"),
        (HELP, "help"),
        (LOCATION, "location"),
    )
    action = models.PositiveSmallIntegerField(choices=ACTIONS)
    text = models.TextField(max_length=10, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Profile, related_name="actions_sender")
    receiver = models.ManyToManyField(Profile, related_name="actions_receiver")

    def __unicode__(self):
        return u"{} {} {}".format(self.sender, self.ACTIONS[self.action], self.text)
