# Generated by Django 4.0 on 2022-12-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productor', '0004_delete_subastatransporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
