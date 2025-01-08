# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Profile(models.Model):

    #__Profile_FIELDS__
    google_calendar_id = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    real_name = models.CharField(max_length=255, null=True, blank=True)

    #__Profile_FIELDS__END

    class Meta:
        verbose_name        = _("Profile")
        verbose_name_plural = _("Profile")


class Agenttype(models.Model):

    #__Agenttype_FIELDS__
    system_message = models.TextField(max_length=255, null=True, blank=True)

    #__Agenttype_FIELDS__END

    class Meta:
        verbose_name        = _("Agenttype")
        verbose_name_plural = _("Agenttype")



#__MODELS__END
