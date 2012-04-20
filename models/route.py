from django.contrib.gis.db import models
from agency import Agency
from source import Source

ROUTETYPES = (
    (0, 'Tram, Streetcar, Light rail'),
    (1, 'Subway, Metro'),
    (2, 'Rail'),
    (3, 'Bus'),
    (4, 'Ferry'),
    (5, 'Cable car'),
    (6, 'Gondola'),
    (7, 'Funicular'),
)

class Route(models.Model):
    class Meta:
        app_label = 'gtfs'

        # Agency and stopId are a natural composite key
        unique_together = (('source', 'routeId'))

    '''
    source id
    '''
    sourceId = models.CharField(max_length=128)
    
    '''
    Source of the stop
    '''
    source = models.ForeignKey(Source)

    '''
    The route_id field contains an ID that uniquely identifies a route.
    The route_id is dataset unique.
    '''
    routeId = models.CharField(max_length=128)

    '''
    agency id
    '''
    agencyId = models.CharField(max_length=128, null=True, blank=True)

    '''
    Agency object foreign key
    '''
    agency = models.ForeignKey(Agency)

    ''' R
    The route_short_name contains the short name of a route.
    This will often be a short, abstract identifier like "32",
    "100X", or "Green" that riders use to identify a route,
    but which doesn't give any indication of what places the
    route serves. If the route does not have a short name,
    please specify a route_long_name and use an empty string
    as the value for this field.
    '''
    routeShortName = models.CharField(max_length=256, blank=True, null=True)

    ''' R
    The route_long_name contains the full name of a route.
    This name is generally more descriptive than the
    route_short_name and will often include the route's
    destination or stop. If the route does not have a
    long name, please specify a route_short_name and
    use an empty string as the value for this field.
    '''
    routeLongName = models.CharField(max_length=1024, blank=True, null=True)

    ''' O
    The route_desc field contains a description of a route.
    Please provide useful, quality information. Do not
    simply duplicate the name of the route. For example,
    "A trains operate between Inwood-207 St, Manhattan
    and Far Rockaway-Mott Avenue, Queens at all times.
    Also from about 6AM until about midnight, additional
    A trains operate between Inwood-207 St and Lefferts
    Boulevard (trains typically alternate between
    Lefferts Blvd and Far Rockaway)."
    '''
    routeDesc = models.CharField(max_length=1024, blank=True, null=True)

    ''' R
    The route_type field describes the type of transportation
    used on a route.
    '''
    routeType = models.IntegerField(choices=ROUTETYPES)

    ''' O
    The route_url field contains the URL of a web page
    about that particular route
    '''
    routeUrl = models.URLField(blank=True, null=True)

    ''' O
    In systems that have colors assigned to routes, the route_color field
    defines a color that corresponds to a route.
    '''
    routeColor = models.CharField(max_length=16, blank=True, null=True)

    '''
    The route_text_color field can be used to
    specify a legible color to use
    for text drawn against a background of route_color
    '''
    routeTextColor = models.CharField(max_length=16, blank=True, null=True)

    def __unicode__(self):
        return u'%s, %s, %s' % (self.source, self.routeId, self.routeLongName)
