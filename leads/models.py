from django.db import models

# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name