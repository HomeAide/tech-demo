from django.db import models

# Create your models here.
class AT(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    location = models.IntegerField()

    def __str__(self):
        return self.name