# Generated by Django 4.0 on 2022-12-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productor', '0003_remove_offer_offerfilename_offer_offerfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='localsale',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='localsale',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
