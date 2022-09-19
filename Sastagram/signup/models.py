from django.db import models

# Create your models here.


class User(models.Model):
    key = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    uname = models.CharField(max_length=255, unique=True)
    number = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return '%s %s' % (self.fname, self.uname)
    class Meta:
        db_table = 'user'
    
