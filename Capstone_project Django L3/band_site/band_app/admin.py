from django.contrib import admin
from .models import BandMember, Event

# Register the BandMember model to make it accessible via the Django
# admin interface.
# The BandMember model typically represents a person who is part of the
# band. It will be managed and displayed in the admin panel.
admin.site.register(BandMember)

# Register the Event model to make it accessible via the Django admin
# interface.
# The Event model generally represents events where the band performs.
# This will also be managed and displayed in the admin panel.
admin.site.register(Event)
