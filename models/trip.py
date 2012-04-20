from django.contrib.gis.db import models
from route import Route
from calendar import Calendar
from agency import Source

DIRECTIONID = (
    (0, 'DIR-0'),
    (1, 'DIR-1'),
)

class Trip(models.Model):
    '''
    Model object representing a Trip (trips.txt)
    '''
    class Meta:
        app_label = 'gtfs'
        unique_together = (('source', 'tripId'))
    
    '''
    source id
    '''
    sourceId = models.CharField(max_length=128)
    
    '''
    Source of the stop
    '''
    source = models.ForeignKey(Source)
    
    ''' R
    The trip_id field contains an ID that identifies a trip. 
    The trip_id is dataset unique.
    '''
    tripId = models.CharField(max_length=128)
    
    '''
    Route id for ease of access
    '''
    routeId = models.CharField(max_length=128)
    
    '''
    Route for this trip
    '''
    route = models.ForeignKey(Route)
    
    '''
    Service id
    '''
    serviceId = models.CharField(max_length=128)
    
    '''
    Service id in the calendar
    '''
    service = models.ForeignKey(Calendar)
    
    ''' O
    The trip_headsign field contains the text that appears 
    on a sign that identifies the trip's destination to 
    passengers. Use this field to distinguish between 
    different patterns of service in the same route. 
    If the headsign changes during a trip, you can 
    override the trip_headsign by specifying values 
    for the the stop_headsign field in stop_times.txt.
    '''
    headSign = models.CharField(max_length=256, null=True, blank=True)
    
    ''' O
    The trip_short_name field contains the text that appears 
    in schedules and sign boards to identify the trip to 
    passengers, for example, to identify train numbers for 
    commuter rail trips. If riders do not commonly rely on 
    trip names, please leave this field blank.

    A trip_short_name value, if provided, should uniquely 
    identify a trip within a service day; it should not be 
    used for destination names or limited/express designations.
    '''
    shortName = models.CharField(max_length=256, null=True, blank=True)
    
    ''' O
    The direction_id field contains a binary value that 
    indicates the direction of travel for a trip. Use 
    this field to distinguish between bi-directional 
    trips with the same route_id. This field is not 
    used in routing; it provides a way to separate 
    trips by direction when publishing time tables. 
    You can specify names for each direction with the 
    trip_headsign field.

    0 - travel in one direction (e.g. outbound travel)
    1 - travel in the opposite direction (e.g. inbound travel)
    
    For example, you could use the trip_headsign and 
    direction_id fields together to assign a name to 
    travel in each direction on trip "1234", the trips.txt 
    file would contain these rows for use in time tables:

    trip_id, ... ,trip_headsign,direction_id
    1234, ... , to Airport,0
    1505, ... , to Downtown,1
    '''
    directionId = models.IntegerField(choices=DIRECTIONID, null=True, blank=True)
    
    '''
    The block_id field identifies the block to which the trip 
    belongs. A block consists of two or more sequential trips 
    made using the same vehicle, where a passenger can 
    transfer from one trip to the next just by staying 
    in the vehicle. The block_id must be referenced by 
    two or more trips in trips.txt.
    '''
    blockId = models.CharField(max_length=128, null=True, blank=True)
    
    ''' O
    The shape_id field contains an ID that defines a shape for the trip
    '''
    shapeId = models.CharField(max_length=128, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s, %s, %s' % (self.tripId, self.routeId, self.headSign)