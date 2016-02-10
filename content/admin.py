from django.contrib import admin
from django import forms
from happenings.models import (Tag,
                               Location,
                               Category,
                               Event,
                               Cancellation)
from happenings.admin import EventAdmin as EventAdminBase
from sorl.thumbnail.admin import AdminImageMixin
from pagedown.widgets import AdminPagedownWidget

from content.models import HoppyUpdate, Announcement


class EventAdmin(EventAdminBase):
    fields = ('start_date', 'end_date', 'all_date', 'repeat',
              'end_repeat', 'title', 'description')
    fieldsets = None
    inlines = []


class HoppyUpdateAdminForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = HoppyUpdate
        exclude = ()


class HoppyUpdateAdmin(AdminImageMixin, admin.ModelAdmin):
    form = HoppyUpdateAdminForm
    prepopulated_fields = {'slug': ['title']}


class AnnouncementAdminForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Announcement
        exclude = ()


class AnnouncementAdmin(AdminImageMixin, admin.ModelAdmin):
    form = AnnouncementAdminForm
    prepopulated_fields = {'slug': ['title']}


admin.site.unregister(Tag)
admin.site.unregister(Location)
admin.site.unregister(Category)
admin.site.unregister(Event)
admin.site.unregister(Cancellation)

admin.site.register(Event, EventAdmin)
admin.site.register(HoppyUpdate, HoppyUpdateAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
