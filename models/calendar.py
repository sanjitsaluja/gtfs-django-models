from django.contrib.gis.db import models
from datetime import datetime
from source import Source

class Calendar(models.Model):
    '''
    Model object representing a service entry (calendar.txt)
    '''
    class Meta:
        app_label = 'gtfs'
        
        # source and stopId are a natural composite key
        unique_together = (('source', 'serviceId'))
        
    '''
    source id
    '''
    sourceId = models.CharField(max_length=128)
    
    '''
    Source of the stop
    '''
    source = models.ForeignKey(Source)
    
    '''
    The service_id contains an ID that uniquely identifies a 
    set of dates when service is available for one or 
    more routes.
    '''
    serviceId = models.CharField(max_length=128)
    
    ''' R
    The monday field contains a binary value that indicates 
    whether the service is valid for all Mondays.
    '''
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    saturday = models.BooleanField()
    sunday = models.BooleanField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __unicode__(self):
        '''
        Return unicode description of this object
        '''
        serviceDays = []
        if self.monday:
            serviceDays.append(u'mon')
        if self.tuesday:
            serviceDays.append(u'tue')
        if self.wednesday:
            serviceDays.append(u'wed')
        if self.thursday:
            serviceDays.append(u'thu')
        if self.friday:
            serviceDays.append(u'fri')
        if self.saturday:
            serviceDays.append(u'sat')
        if self.sunday:
            serviceDays.append(u'sun')
        return "%s, %s" % (self.serviceId, u','.join(serviceDays))
    
    def today(self):
        '''
        bool if the service is on today or false otherwise
        '''
        
        #Degenerate input
        if not self.monday and not self.tuesday and not self.wednesday and not self.thursday and not self.friday and not self.saturday and not self.sunday:
            return True
        
        weekday = datetime.now().isoweekday()
        print weekday, self.tuesday
        if weekday is 1:
            return self.monday
        elif weekday is 2:
            return self.tuesday
        elif weekday is 3:
            return self.wednesday
        elif weekday is 4:
            return self.thursday
        elif weekday is 5:
            return self.friday
        elif weekday is 6:
            return self.saturday
        else:
            return self.sunday