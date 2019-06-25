from django.db import models


class Card(models.Model):
    score = models.CharField(min_length=20)
