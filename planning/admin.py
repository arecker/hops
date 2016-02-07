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

from planning.models import HoppyUpdate


class EventAdmin(EventAdminBase):
    fieldsets = ((None, {'fields': ('start_date', 'end_date', 'all_day', 'repeat',
                                    'end_repeat', 'title', 'description',
                                    'created_by',)}),)


class HoppyUpdateAdminForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = HoppyUpdate
        exclude = ()


class HoppyUpdateAdmin(AdminImageMixin, admin.ModelAdmin):
    form = HoppyUpdateAdminForm
    prepopulated_fields = {'slug': ['title']}


admin.site.unregister(Tag)
admin.site.unregister(Location)
admin.site.unregister(Category)
admin.site.unregister(Event)
admin.site.unregister(Cancellation)

admin.site.register(Event, EventAdmin)
admin.site.register(HoppyUpdate, HoppyUpdateAdmin)
