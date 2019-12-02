from django.db import models


class MagicNumber(models.Model):
    number = models.IntegerField()
