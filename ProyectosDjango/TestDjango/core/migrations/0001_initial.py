# Generated by Django 4.0.4 on 2022-06-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consultas'], [1, 'reclamos'], [2, 'sugerencias'], [3, 'otros']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('categoria', models.CharField(max_length=32)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('idusuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id usuario')),
                ('nombreusuario', models.CharField(max_length=50)),
                ('apellidousuario', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]
