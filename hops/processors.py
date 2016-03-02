from django.conf import settings as django_settings

from content.models import Partner


def settings(request):
    ctx = {}

    constants = ('CURATOR_EMAIL', 'DEBUG', 'DOMAIN',
                 'GITHUB_URL', 'WIKI_URL', 'NON_PROFIT_ID',
                 'FACEBOOK_URL', 'GOOGLE_MAPS_URL', 'INSTAGRAM_URL',
                 'TWITTER_URL')

    for k in constants:
        ctx[k] = getattr(django_settings, k, None)

    return ctx


def advertisement(request):
    return {'ad': Partner.objects.pluck()}


def path(request):
    if django_settings.DEBUG:
        return {'CURRENT_PAGE': 'testing.com'}
    return {'CURRENT_PAGE': request.get_full_path()}


def analytics(request):
    if not django_settings.DEBUG:
        value = getattr(django_settings,'GOOGLE_ANALYTICS_ID', None)
        return {'GOOGLE_ANALYTICS_ID': value}
    return {}
