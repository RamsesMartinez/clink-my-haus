from django.conf import settings


def envs(request):
    return {'GOOGLEMAPS_KEY': settings.DJANGO_GOOGLEMAPS_KEY}
