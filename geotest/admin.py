from django.contrib.gis import admin

from .models import Friend

admin.site.register(Friend, admin.OSMGeoAdmin)

