from django.contrib import admin
from happenings.models import (Tag,
                               Location,
                               Category,
                               Event)
from happenings.admin import EventAdmin as EventAdminBase


class EventAdmin(EventAdminBase):
    fieldsets = ((None, {'fields': ('start_date', 'end_date', 'all_day', 'repeat',
                                    'end_repeat', 'title', 'description',
                                    'created_by',)}),
                 ('Color', {'classes': ('collapse',),
                            'fields': (('background_color', 'background_color_custom'),
                                       ('font_color', 'font_color_custom'),)}),)


admin.site.unregister(Tag)
admin.site.unregister(Location)
admin.site.unregister(Category)
admin.site.unregister(Event)

admin.site.register(Event, EventAdmin)
