# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tamano', models.IntegerField()),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('dimension', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=40)),
                ('numero_lotes', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DUENO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='JEFE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('cultivo', models.ForeignKey(to='proyecto.Cultivo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TRABAJADOR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('genero', models.IntegerField(default=1, choices=[(1, b'masculino'), (2, b'femenino')])),
                ('tipoDocumento', models.IntegerField(default=1, choices=[(1, b'cedula ciudadania'), (2, b'cedula extranjera')])),
                ('numero_Documento', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=40)),
                ('tipo_usuario', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='trabajador',
            name='documento',
            field=models.OneToOneField(to='proyecto.USUARIO'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='jefe',
            field=models.ForeignKey(to='proyecto.JEFE'),
        ),
        migrations.AddField(
            model_name='lote',
            name='trabajador',
            field=models.ForeignKey(to='proyecto.TRABAJADOR', null=True),
        ),
        migrations.AddField(
            model_name='jefe',
            name='documento',
            field=models.OneToOneField(to='proyecto.USUARIO'),
        ),
        migrations.AddField(
            model_name='jefe',
            name='dueno',
            field=models.ForeignKey(to='proyecto.DUENO'),
        ),
        migrations.AddField(
            model_name='dueno',
            name='documento',
            field=models.OneToOneField(to='proyecto.USUARIO'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='dueno',
            field=models.ForeignKey(to='proyecto.DUENO', null=True),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='jefe',
            field=models.OneToOneField(null=True, to='proyecto.JEFE'),
        ),
    ]
