# Generated by Django 3.0.2 on 2020-01-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('project_name', models.CharField(help_text='Nombre del proyecto', max_length=120, verbose_name='Proyecto')),
                ('url_location', models.URLField(blank=True, help_text='URL de Google Maps con la ubicación, asegúrese de que sea una dirección valida.', max_length=300, null=True, verbose_name='Url de Ubicación')),
                ('address', models.CharField(blank=True, help_text='Dirección obtenida de la Url de Google Maps. Se generará automáticamente', max_length=300, null=True, verbose_name='Dirección')),
                ('latitude', models.CharField(blank=True, help_text='Deje este campo vacío, se calculará con la url de Google Maps', max_length=20, null=True, verbose_name='Latitud')),
                ('longitude', models.CharField(blank=True, help_text='Deje este campo vacío, se calculará con la url de Google Maps', max_length=20, null=True, verbose_name='Longitud')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Fecha de entrega')),
                ('immediate_delivery', models.BooleanField(default=True, help_text='Tiene entrega inmediata', verbose_name='Entrega Inmediata')),
                ('slug', models.SlugField(blank=True, help_text='Puede dejar el campo vacío, se generará automáticamente.', max_length=120, unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True, help_text='Proyecto activo', verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('state_name', models.CharField(max_length=120, verbose_name='Nombre de Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='TownHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('town_hall_name', models.CharField(max_length=120, verbose_name='Nombre de Alcaldía')),
                ('state', models.ForeignKey(help_text='Elija un Estado', on_delete=django.db.models.deletion.CASCADE, to='projects.State', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Alcaldía',
                'verbose_name_plural': 'Alcaldías',
            },
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('suburb_name', models.CharField(max_length=120, verbose_name='Colonia')),
                ('town_hall', models.ForeignKey(help_text='Elija una Alcaldía', on_delete=django.db.models.deletion.CASCADE, to='projects.TownHall', verbose_name='Alcaldía')),
            ],
            options={
                'verbose_name': 'Colonia',
                'verbose_name_plural': 'Colonias',
            },
        ),
        migrations.CreateModel(
            name='ProjectVariants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('area', models.FloatField(default=1, verbose_name='Superficie')),
                ('habitable_area', models.FloatField(blank=True, default=1, null=True, verbose_name='Superficie Habitable')),
                ('number_of_bedrooms', models.FloatField(default=1, help_text='Número de cuartos (Ej. 1, 1.5, 2, etc)', verbose_name='Cuartos')),
                ('number_of_bathrooms', models.FloatField(default=1, help_text='Número de Baños (Ej. 1, 1.5, 2, etc)', verbose_name='Baños')),
                ('number_of_parking_lots', models.PositiveIntegerField(default=1, help_text='Cajones de estacionamiento', verbose_name='Estacionamiento')),
                ('has_comunal_roof', models.BooleanField(default=False, help_text='Tiene Roof Comunal', verbose_name='Rof Garden Comunal')),
                ('has_private_roof', models.BooleanField(default=False, help_text='Tiene Roof Privado', verbose_name='Rof Garden Privado')),
                ('private_roof_size', models.FloatField(default=0, verbose_name='Tamaño del Roof Garden Privado')),
                ('comunal_roof_size', models.FloatField(default=0, verbose_name='Tamaño del Roof Garden Comunal')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=13, verbose_name='Precio')),
                ('project', models.ForeignKey(help_text='Elija un proyecto', on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Variante de proyecto',
                'verbose_name_plural': 'Variantes de proyectos',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('has_lobby', models.BooleanField(default=False, help_text='Tiene Roof Comunal', verbose_name='Lobby')),
                ('has_elevator', models.BooleanField(default=False, help_text='Tiene Elevador', verbose_name='Elevador')),
                ('has_surveillance', models.BooleanField(default=False, help_text='Tiene Vigilancia', verbose_name='Vigilancia')),
                ('has_cellar', models.BooleanField(default=False, help_text='Tiene Bodega', verbose_name='Bodega')),
                ('has_gym', models.BooleanField(default=False, help_text='Tiene Gimnasio', verbose_name='Gimnasio')),
                ('has_dining_kitchen', models.BooleanField(default=True, help_text='Tiene Cocina/Comedor', verbose_name='Cocina/Comedor')),
                ('has_integrated_kitchen', models.BooleanField(default=True, help_text='Tiene Cocina Integrada', verbose_name='Cocina Integrada')),
                ('has_closed_circuit', models.BooleanField(default=False, help_text='Tiene Circuito Cerrado', verbose_name='Circuito Cerrado')),
                ('has_swimming_pool', models.BooleanField(default=False, help_text='Tiene Alberca', verbose_name='Alberca')),
                ('has_business_center', models.BooleanField(default=False, help_text='Tiene Business Center', verbose_name='Business Center')),
                ('project', models.OneToOneField(help_text='Elija un proyecto', on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProjectRenders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Render del Proyecto')),
                ('project', models.ForeignKey(help_text='Elija un proyecto', on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Render',
                'verbose_name_plural': 'Renders',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProjectConstructionPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'verbose_name': 'Plano de Construcción',
                'verbose_name_plural': 'Planos de Construcción',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='suburb',
            field=models.ForeignKey(help_text='Elija una colonia', on_delete=django.db.models.deletion.CASCADE, to='projects.Suburb', verbose_name='Colonia'),
        ),
    ]
