from django.conf import settings as django_settings

from content.models import BannerAdvertisement


def settings(request):
    return {'CURATOR_EMAIL': django_settings.CURATOR_EMAIL,
            'DEBUG': django_settings.DEBUG,
            'DOMAIN': django_settings.DOMAIN}


def advertisement(request):
    return {'ad': BannerAdvertisement.objects.pluck()}


def path(request):
    if django_settings.DEBUG:
        return {'CURRENT_PAGE': 'testing.com'}
    return {'CURRENT_PAGE': request.get_full_path()}


def analytics(request):
    if not django_settings.DEBUG:
        value = getattr(django_settings,'GOOGLE_ANALYTICS_ID', None)
        return {'GOOGLE_ANALYTICS_ID': value}
    return {}
