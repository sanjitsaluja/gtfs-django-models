from django.contrib.gis.db import models
from route import Route
from stop import Stop
from trip import Trip
from agency import Source

class StopTime(models.Model):
    '''
    Model object representing stop_times.txt
    '''
    class Meta:
        app_label = 'gtfs'
        unique_together = (('source', 'tripId', 'stopId', 'stopSequence'))
    
    '''
    source id
    '''
    sourceId = models.CharField(max_length=128)
    
    '''
    Source of the stop
    '''
    source = models.ForeignKey(Source)
    
    '''
    Trip id for ease of access. identifies the vehicle stop times
    '''
    tripId = models.CharField(max_length=128)
    trip = models.ForeignKey(Trip)
    
    '''
    Route id for ease of access
    '''
    routeId = models.CharField(max_length=128)
    route = models.ForeignKey(Route)
    
    '''
    The stop obj field contains an ID that uniquely 
    identifies a stop. Multiple routes may use the same stop
    '''
    stopId = models.CharField(max_length=128)
    stop = models.ForeignKey(Stop)
    
    '''
    The arrival_time specifies the arrival time at a specific 
    stop for a specific trip on a route. The time is measured 
    from "noon minus 12h" (effectively midnight, except for 
    days on which daylight savings time changes occur) at 
    the beginning of the service date. For times occurring 
    after midnight on the service date, enter the time as a 
    value greater than 24:00:00 in HH:MM:SS local time for 
    the day on which the trip schedule begins. If you 
    don't have separate times for arrival and departure 
    at a stop, enter the same value for arrival_time 
    and departure_time.

    You must specify arrival times for the first and 
    last stops in a trip. If this stop isn't a time 
    point, use an empty string value for the 
    arrival_time and departure_time fields. Stops 
    without arrival times will be scheduled based 
    on the nearest preceding timed stop. To ensure 
    accurate routing, please provide arrival and 
    departure times for all stops that are time 
    points. Do not interpolate stops.

    Times must be eight digits in HH:MM:SS 
    format (H:MM:SS is also accepted, 
    if the hour begins with 0). Do not 
    pad times with spaces. The following 
    columns list stop times for a trip and t
    he proper way to express those times in 
    the arrival_time field:

    Time    arrival_time value
    08:10:00 A.M.    08:10:00 or 8:10:00
    01:05:00 P.M.    13:05:00
    07:40:00 P.M.    19:40:00
    01:55:00 A.M.    25:55:00
    
    Note: Trips that span multiple dates will 
    have stop times greater than 24:00:00. For example, 
    if a trip begins at 10:30:00 p.m. and ends at 
    2:15:00 a.m. on the following day, the stop 
    times would be 22:30:00 and 26:15:00. 
    Entering those stop times as 22:30:00 
    and 02:15:00 would not produce the desired results.
    '''
    arrivalSeconds = models.IntegerField()
    
    # The arrival_time specifies the dep time at a 
    # specific stop for a specific trip on a route.
    # The time is measured from "noon minus 12h
    departureSeconds = models.IntegerField()
    
    
    # The stop_sequence field identifies the order of the 
    # stops for a particular trip.
    stopSequence = models.IntegerField()
    headSign = models.CharField(max_length=256, null=True, blank=True)
    pickUpType = models.IntegerField(null=True, blank=True)
    dropOffType = models.IntegerField(null=True, blank=True)
    
    ''' O
    When used in the stop_times.txt file, the 
    shape_dist_traveled field positions a stop as a 
    distance from the first shape point. 
    The shape_dist_traveled field represents a 
    real distance traveled along the route in 
    units such as feet or kilometers. For example, 
    if a bus travels a distance of 5.25 kilometers 
    from the start of the shape to the stop, the 
    shape_dist_traveled for the stop ID would be 
    entered as "5.25". This information allows the 
    trip planner to determine how much of the shape 
    to draw when showing part of a trip on the map. 
    The values used for shape_dist_traveled must 
    increase along with stop_sequence: they cannot 
    be used to show reverse travel along a route.
    '''
    shapeDistanceTraveled = models.FloatField(null=True, blank=True)
        
    def __unicode__(self):
        return u'%s: %s, %s, %s' % (self.source, self.routeId, self.headSign, self.stop.stopName)
    
    
    def displayHeadSign(self):
        return self.headSign or self.trip.headSign

