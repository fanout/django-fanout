from django.conf import settings
import fanout

if hasattr(settings, 'FANOUT_REALM'):
	fanout.realm = settings.FANOUT_REALM
if hasattr(settings, 'FANOUT_KEY'):
	fanout.key = settings.FANOUT_KEY

def publish(channel, data, id=None, prev_id=None, blocking=False, callback=None):
	fanout.publish(channel, data, id, prev_id, blocking, callback)
