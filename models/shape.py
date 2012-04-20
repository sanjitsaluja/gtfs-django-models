from django.contrib.gis.db import models
from source import Source

class Shape(models.Model):
    class Meta:
        app_label = 'gtfs'
        unique_together = (('source', 'shapeId', 'sequence'))
    
    '''
    Model object represeting a Shape (shapes.txt)
    '''
    source = models.ForeignKey(Source)
    shapeId = models.CharField(max_length=128)
    lat = models.FloatField()
    lng = models.FloatField()
    point = models.PointField()
    
    ''' R
    The shape_pt_sequence field associates the latitude 
    and longitude of a shape point with its sequence 
    order along the shape. The values for 
    shape_pt_sequence must be non-negative integers, 
    and they must increase along the trip.
    
    For example, if the shape "A_shp" has three points 
    in its definition, the shapes.txt file might contain 
    these rows to define the shape:

    A_shp,37.61956,-122.48161,0
    A_shp,37.64430,-122.41070,6
    A_shp,37.65863,-122.30839,11
    '''
    sequence = models.IntegerField()
    distanceTraveled = models.FloatField(null=True, blank=True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u"%s %d" % (self.shapeId, self.sequence)
