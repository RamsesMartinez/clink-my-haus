from django.db import models

from clinkmyhaus.apps.utils.models import CHouseModel


class State(CHouseModel):
    state_name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return "{}".format(self.state_name)


class Locality(CHouseModel):
    locality_name = models.CharField(max_length=120)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

    def __str__(self):
        return "{}".format(self.locality_name)
