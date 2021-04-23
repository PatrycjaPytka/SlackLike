from django.db import models
from django.contrib.auth.models import User


class Groups(models.Model):
    name_of_group = models.CharField(max_length=50, blank=False, unique=True)
    members = models.ManyToManyField(User, blank=True, related_name='access')

    def __str__(self):
        return self.name_of_group
