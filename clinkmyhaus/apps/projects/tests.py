from django.test import TestCase

from clinkmyhaus.apps.projects.models.addresses import Suburb, TownHall, State
from clinkmyhaus.apps.projects.models.projects import Project


class ProjectTestCase(TestCase):

    def setUp(self):
        state = State.objects.create(state_name='Estado de prueba')
        town_hall = TownHall.objects.create(town_hall_name='Alcandía Prueba', state=state)
        suburb = Suburb.objects.create(suburb_name='Colonia de Prueba', town_hall=town_hall)
        Project.objects.create(project_name='Proyecto prueba', suburb=suburb)
        Project.objects.create(project_name='Proyecto prueba', suburb=suburb)

    def test_check_slugs(self):
        object_1 = Project.objects.get(pk=1)
        object_2 = Project.objects.get(pk=2)

        self.assertEqual(object_1.slug, 'proyecto-prueba')
        self.assertEqual(object_2.slug, 'proyecto-prueba-2')

