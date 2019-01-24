from django.db import models
from django.conf import settings


class TimeMixIn(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class State(models.Model):  # Judete
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):  # Orase
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ong(models.Model, TimeMixIn):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, default=None, help_text="An organisation can be managed by an user")
    name = models.CharField(max_length=200)
    cif = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    bank_account = models.CharField(max_length=24, blank=True, help_text="In order to be valid, it should have a bank account")

    def __str__(self):
        return self.name
