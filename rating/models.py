from django.db import models

# Create your models here.
class Rating(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField(blank=False)
    data = models.DateTimeField(auto_now_add=True)

