# Generated by Django 4.2.3 on 2023-07-27 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0004_rename_id_categoria_articulo_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]