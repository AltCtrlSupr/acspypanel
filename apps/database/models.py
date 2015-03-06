from django.db import models
from ..common.models import ACSModelBase


class Database(ACSModelBase):
    name = models.CharField(max_length=64)
    # Service


class DatabaseUser(ACSModelBase):
    database = models.ForeignKey(Database)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=250)
