# Generated by Django 4.2.3 on 2023-07-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentarios', '0004_alter_comentario_fecha_edicion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_edicion',
            field=models.DateTimeField(null=True),
        ),
    ]
