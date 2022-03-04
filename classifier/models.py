from django.db import models

# Create your models here.
class Classification(models.Model):
    image_src = models.CharField(max_length=500)
    result = models.CharField(max_length=30)
    
