from django.db import models

from clinkmyhaus.apps.utils.models import CHouseModel


class State(CHouseModel):
    state_name = models.CharField(
        max_length=120,
        verbose_name='Nombre de Estado'
    )

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return '{}'.format(self.state_name)


class TownHall(CHouseModel):
    town_hall_name = models.CharField(
        max_length=120,
        verbose_name='Nombre de Alcaldía'
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        verbose_name='Estado',
        help_text='Elija un Estado'
    )

    class Meta:
        verbose_name = 'Alcaldía'
        verbose_name_plural = 'Alcaldías'

    def __str__(self):
        return '{}'.format(self.town_hall_name)


class Suburb(CHouseModel):
    suburb_name = models.CharField(
        max_length=120,
        verbose_name='Colonia'
    )
    town_hall = models.ForeignKey(
        TownHall,
        on_delete=models.CASCADE,
        verbose_name='Alcaldía',
        help_text='Elija una Alcaldía'
    )

    class Meta:
        verbose_name = 'Colonia'
        verbose_name_plural = 'Colonias'

    def __str__(self):
        return '{}'.format(self.suburb_name)
