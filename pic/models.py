from django.db import models

# Create your models here.


class Infor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    class Meta:
        unique_together = ("name", "type")


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, unique=True)
