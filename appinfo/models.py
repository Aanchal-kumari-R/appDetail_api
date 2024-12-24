from django.db import models

# Create your models here.
class AppData(models.Model):  

    def __str__(self):
        return self.app_name 
    
    app_name = models.CharField(max_length=100) 
    version = models.FloatField() 
    description = models.TextField()