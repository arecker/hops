import pytz

from django.utils import timezone

class Timezone(object):
    def process_request(self, request):
        try:
            timezone.activate(pytz.timezone('America/Chicago'))
        except:                 # all operations in the midwest
            pass                # just force everything into that zone
