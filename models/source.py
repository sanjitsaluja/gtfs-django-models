from django.contrib.gis.db import models

class Source(models.Model):
    '''
    Model object representing an import source. One particular data feed.
    '''
    class Meta:
        app_label = 'gtfs'
    
    '''
    id of the source.
    '''
    sourceId = models.CharField(max_length=128, primary_key=True)
       
    '''
    Data source code name. friendly name.
    '''
    codeName= models.CharField(max_length=256)
       
    '''
    Url of the gtfs zip
    ''' 
    importUrl = models.URLField()
    
    '''
    Date when the gtfs data source was last imported
    '''
    updated = models.DateField(auto_now=True)
    
    '''
    Date when the gtfs data source was first imported
    '''
    created = models.DateField(auto_now_add=True)
        
    def __unicode__(self):
        return u'%s:%s' % (self.sourceId, self.codeName)