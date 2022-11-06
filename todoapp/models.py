from django.db import models

# Create your models here.

class Task_db(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    date = models.DateField()

    def __str__(self):   #it is used to change the visible name of the field in database
        return self.title