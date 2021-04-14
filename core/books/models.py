from django.db import models
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()

    def __str__(self):
        return self.title
    