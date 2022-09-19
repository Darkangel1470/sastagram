from django.db import models

# Create your models here.
class User(models.Model):
    key = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    number = models.IntegerField()
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'user'
