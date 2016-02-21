from django.conf import settings as django_settings

from content.models import BannerAdvertisement


def settings(request):
    return {'CURATOR_EMAIL': django_settings.CURATOR_EMAIL,
            'DEBUG': django_settings.DEBUG}


def advertisement(request):
    return {'ad': BannerAdvertisement.objects.pluck()}


def path(request):
    if django_settings.DEBUG:
        return {'CURRENT_PAGE': 'testing.com'}
    return {'CURRENT_PAGE': request.get_full_path()}
