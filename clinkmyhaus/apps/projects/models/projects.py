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
    url_location = models.URLField(
        max_length=300,
        verbose_name='Url de Ubicación',
        help_text='URL de Google Maps con la ubicación, asegúrese de que sea una dirección valida.',
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Dirección',
        help_text='Dirección obtenida de la Url de Google Maps. Se generará automáticamente',
        blank=True,
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
    delivery_date = models.DateField(
        verbose_name='Fecha de entrega',
        blank=True,
        null=True
    )
    immediate_delivery = models.BooleanField(
        verbose_name='Entrega Inmediata',
        help_text='Tiene entrega inmediata',
        default=True
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        verbose_name='Slug',
        help_text='Puede dejar el campo vacío, se generará automáticamente.'
    )
    has_comunal_roof = models.BooleanField(
        default=False,
        verbose_name='Rof Garden Comunal',
        help_text='Tiene Roof Comunal'
    )
    has_private_roof = models.BooleanField(
        default=False,
        verbose_name='Rof Garden Privado',
        help_text='Tiene Roof Privado'
    )
    private_roof_size = models.FloatField(
        default=0,
        verbose_name='Tamaño del Roof Garden Privado'
    )
    comunal_roof_size = models.FloatField(
        default=0,
        verbose_name='Tamaño del Roof Garden Comunal'
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


class ProjectVariants(CHouseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='Proyecto',
        help_text='Elija un proyecto'
    )
    area = models.FloatField(
        default=1,
        verbose_name='Superficie'
    )
    habitable_area = models.FloatField(
        default=1,
        verbose_name='Superficie Habitable',
        blank=True,
        null=True
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
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=13,
        verbose_name='Precio',
    )

    class Meta:
        verbose_name = 'Variante de proyecto'
        verbose_name_plural = 'Variantes de proyectos'
        ordering = ('id',)

    def __str__(self):
        return '{} - '.format(self.project.project_name, self.id)


class ProjectServices(CHouseModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='Proyecto',
        help_text='Elija un proyecto'
    )
    has_lobby = models.BooleanField(
        default=False,
        verbose_name='Lobby',
        help_text='Tiene Roof Comunal'
    )
    has_elevator = models.BooleanField(
        default=False,
        verbose_name='Elevador',
        help_text='Tiene Elevador'
    )
    has_surveillance = models.BooleanField(
        default=False,
        verbose_name='Vigilancia',
        help_text='Tiene Vigilancia'
    )
    has_cellar = models.BooleanField(
        default=False,
        verbose_name='Bodega',
        help_text='Tiene Bodega'
    )
    has_gym = models.BooleanField(
        default=False,
        verbose_name='Gimnasio',
        help_text='Tiene Gimnasio'
    )
    has_dining_kitchen = models.BooleanField(
        default=True,
        verbose_name='Cocina/Comedor',
        help_text='Tiene Cocina/Comedor'
    )
    has_integrated_kitchen = models.BooleanField(
        default=True,
        verbose_name='Cocina Integrada',
        help_text='Tiene Cocina Integrada'
    )
    has_closed_circuit = models.BooleanField(
        default=False,
        verbose_name='Circuito Cerrada',
        help_text='Tiene Circuito Cerrado'
    )
    has_swimming_pool = models.BooleanField(
        default=False,
        verbose_name='Alberca',
        help_text='Tiene Alberca'
    )
    has_business_center = models.BooleanField(
        default=False,
        verbose_name='Business Center',
        help_text='Tiene Business Center'
    )
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ('id',)

    def __str__(self):
        return '{} - '.format(self.project.project_name, self.id)


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
    if instance.url_location is not None:
        geocode = utils.get_geocode(instance.url_location)
        instance.address = geocode['formatted_address']
        instance.latitude = geocode['geometry']['location']['lat']
        instance.longitude = geocode['geometry']['location']['lng']
    elif instance.address is not None:
        geocode = utils.get_geocode(instance.address)
        instance.address = geocode['formatted_address']
        instance.latitude = geocode['geometry']['location']['lat']
        instance.longitude = geocode['geometry']['location']['lng']
    else:
        instance.url_location = None
        instance.latitude = None
        instance.longitude = None


@receiver(pre_save, sender=Project)
def project_habitable_area_save(sender, instance, *args, **kwargs):
    """Check if the habitable area is null."""
    if instance.habitable_area is None:
        instance.habitable_area = instance.area
