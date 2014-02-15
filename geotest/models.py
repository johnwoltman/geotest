from django.db import models

class Friend(models.Model):
  '''A friend'''
  first_name = models.CharField(max_length=16, blank=False)
  last_name = models.CharField(max_length=16, blank=False)
  
