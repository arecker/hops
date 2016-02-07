from django.conf import settings as django_settings


def settings(request):
    return {'CURATOR_EMAIL': django_settings.CURATOR_EMAIL}
