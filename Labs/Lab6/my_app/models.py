from django.db import models


class User2(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Airlines(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


