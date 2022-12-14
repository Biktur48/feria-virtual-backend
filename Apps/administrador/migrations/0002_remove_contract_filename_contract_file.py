# Generated by Django 4.0 on 2022-12-12 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='fileName',
        ),
        migrations.AddField(
            model_name='contract',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]