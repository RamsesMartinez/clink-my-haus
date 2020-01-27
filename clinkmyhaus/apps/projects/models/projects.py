import requests
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from clinkmyhaus.apps.projects.models.addresses import Suburb
from clinkmyhaus.apps.utils import utils
from clinkmyhaus.apps.utils.models import CHouseModel
from clinkmyhaus.apps.utils.utils import random_pic, unique_slug_generator
from config.settings.base import DJANGO_GOOGLEMAPS_KEY


class Project(CHouseModel):
    project_name = models.CharField(
        max_length=120,
        verbose_name='Proyecto',
        help_text='Nombre del proyecto'
    )
    suburb = models.ForeignKey(
        Suburb,
        on_delete=models.CASCADE,
        verbose_name='Colonia',
        help_text='Elija una colonia'
    )
    number_of_bedrooms = models.FloatField(
        default=1,
        verbose_name='Cuartos',
        help_text='Número de cuartos (Ej. 1, 1.5, 2, etc)'
    )
    number_of_bathrooms = models.FloatField(
        default=1, verbose_name='Baños',
        help_text='Número de Baños (Ej. 1, 1.5, 2, etc)'
    )
    number_of_parking_lots = models.PositiveIntegerField(
        default=1,
        verbose_name='Estacionamiento',
        help_text='Cajones de estacionamiento'
    )
    url_location = models.URLField(
        max_length=300,
        verbose_name='Ubicación',
        help_text='URL de Google Maps con la ubicación, asegúrese de que sea una dirección valida.',
        blank=False,
        null=True
    )
    latitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Latitud',
        help_text='Deje este campo vacío, se calculará con la url de Google Maps'
    )
    longitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Longitud',
        help_text='Deje este campo vacío, se calculará con la url de Google Maps'
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        verbose_name='Slug',
        help_text='Puede dejar el campo vacío, se generará automáticamente.'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text='Proyecto activo'
    )

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ('id',)

    def __str__(self):
        return '{}'.format(self.project_name)

    @property
    def static_pic(self):
        return 'pic%s' % random_pic(1, 14)


class ProjectRenders(CHouseModel):
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Render del Proyecto'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='Proyecto',
        help_text='Elija un proyecto'
    )

    class Meta:
        verbose_name = 'Render'
        verbose_name_plural = 'Renders'
        ordering = ['-id']

    def __str__(self):
        return '{}'.format(self.id)


class ProjectConstructionPlans(CHouseModel):
    image = models.ImageField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Plano de Construcción'
        verbose_name_plural = 'Planos de Construcción'

    def __str__(self):
        return '{}'.format(self.id)


@receiver(pre_save, sender=Project)
def project_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.project_name, instance.slug)


@receiver(pre_save, sender=Project)
def project_latitud_longitude_save(sender, instance, *args, **kwargs):
    """Check from the google maps api the latitude and longitude of the inserted address."""
    geocode = utils.get_geocode(instance.url_location)
    if geocode is not None:
        instance.latitude = geocode['geometry']['location']['lat']
        instance.longitude = geocode['geometry']['location']['lng']
    else:
        instance.url_location = None
        instance.latitude = None
        instance.longitude = None
