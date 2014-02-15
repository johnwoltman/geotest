from django.contrib.gis.db import models

class Friend(models.Model):
  '''A friend'''
  first_name = models.CharField(max_length=16, blank=False)
  last_name = models.CharField(max_length=16, blank=False)


class House(models.Model):
  # Custom GeoDjango manager
  objects = models.GeoManager()
  
  # Fields
  city = models.CharField(max_length=16, blank=False)
  friend = models.ForeignKey(Friend)
  location = models.PointField(geography=True)

