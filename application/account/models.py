from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField

from fcm_django.models import FCMDevice

from core.models import TimeMixIn


class User(AbstractUser, TimeMixIn):
    local_store = models.BooleanField(default=False, help_text="If users does not want to store on server, then store in browser local storage")
    valid_email = models.BooleanField(default=False, help_text="If users wants to receive email they should validate email")
    user_data = JSONField(blank=True, null=True, default=None, help_text="This field is used to store user data required for form completion")
    push_device = models.OneToOneField(FCMDevice, on_delete=models.SET_NULL, blank=True)
    enable_pushes = models.BooleanField(default=False, help_text="If user wants, they can receive reminders on the device app")

    def __str__(self):
        return self.get_full_name() or self.username

