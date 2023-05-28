from django.db import models

# Create your models here.
class Alphabets(models.Model):
    alphabet = models.CharField(max_length=10)
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word