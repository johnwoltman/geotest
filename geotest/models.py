from django.contrib.gis.db import models

class Friend(models.Model):
  '''A friend'''

  # Custom GeoDjango manager
  objects = models.GeoManager()

  first_name = models.CharField(max_length=16, blank=False)
  last_name = models.CharField(max_length=16)
  
  # Where does your friend live?
  street_address = models.CharField(max_length=16)
  city = models.CharField(max_length=16)
  location = models.PointField(geography=True)

  def __unicode__(self):
     return self.first_name

