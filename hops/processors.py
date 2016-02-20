from django.conf import settings as django_settings

from content.models import BannerAdvertisement


def settings(request):
    return {'CURATOR_EMAIL': django_settings.CURATOR_EMAIL,
            'DEBUG': django_settings.DEBUG}


def advertisement(request):
    return {'ad': BannerAdvertisement.objects.pluck()}
