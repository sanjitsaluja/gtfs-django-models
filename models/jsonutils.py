import json
from stop import Stop

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)
class ModelJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stop):
            return {
                'sourceId': obj.sourceId,
                'stopId' : obj.stopId,
                'stopName' : obj.stopName,
                'lat' : obj.lat,
                'lng' : obj.lng
                }
        elif obj is None or isinstance(obj, SIMPLE_TYPES):
            return json.JSONEncoder.default(self, obj)
        else:
            print obj.__class__
            return ''

