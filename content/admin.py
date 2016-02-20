from django.contrib import admin
from django import forms
from sorl.thumbnail.admin import AdminImageMixin
from pagedown.widgets import AdminPagedownWidget

from content.models import (HoppyUpdate,
                            Announcement,
                            Gallery,
                            GalleryImage,
                            BannerAdvertisement,
                            NewspaperArchive,
                            Event)


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


class GalleryImageAdmin(AdminImageMixin, admin.TabularInline):
    model = GalleryImage
    extra = 1


class GalleryForm(forms.ModelForm):
    body = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Gallery
        exclude = ()


class GalleryAdmin(AdminImageMixin, admin.ModelAdmin):
    form = GalleryForm
    prepopulated_fields = {'slug': ['title']}
    inlines = [GalleryImageAdmin]

    class Meta:
        model = Gallery
        exclude = ()


class BannerAdvertisementAdmin(AdminImageMixin, admin.ModelAdmin):
    class Meta:
        model = BannerAdvertisement
        exclude = ()


class NewspaperArchiveAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

    class Meta:
        model = NewspaperArchive
        exclude = ()


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')
    prepopulated_fields = {'slug': ['title']}

    class Meta:
        model = Event
        exclude = ()


admin.site.register(HoppyUpdate, HoppyUpdateAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(BannerAdvertisement, BannerAdvertisementAdmin)
admin.site.register(NewspaperArchive, NewspaperArchiveAdmin)
admin.site.register(Event, EventAdmin)
