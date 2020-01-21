from django.db import models

from clinkmyhaus.apps.projects.models.addresses import Suburb
from clinkmyhaus.apps.utils.models import CHouseModel
from clinkmyhaus.apps.utils.utils import random_pic


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
        default=1,verbose_name='Baños',
        help_text='Número de Baños (Ej. 1, 1.5, 2, etc)'
    )
    number_of_parking_lots = models.PositiveIntegerField(
        default=1,
        verbose_name='Estacionamiento',
        help_text='Cajones de estacionamiento'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
        help_text='Proyecto activo'
    )

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return '{}'.format(self.project_name)

    @property
    def static_pic(self):
        return 'pic%s' % random_pic(1, 14)


class ProjectRenders(CHouseModel):
    image = models.ImageField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Render'
        verbose_name_plural = 'Renders'

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
