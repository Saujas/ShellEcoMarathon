from django.db import models


class Detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name
