# Generated by Django 4.0 on 2022-11-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_contrato_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
