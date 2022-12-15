# Generated by Django 4.0 on 2022-12-14 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('type', models.CharField(choices=[('LOCAL TRADER', 'local trader'), ('INTERNATIONAL TRADER', 'INTERNATIONAL TRADER'), ('CONSULTANR', 'consultant'), ('PRODUCER', 'producer'), ('CARRIER', 'carrier'), ('ADMINISTRATOR', 'administrator')], default='LOCAL TRADER', max_length=30)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
                ('businessName', models.CharField(max_length=50, unique=True)),
                ('documentNumber', models.CharField(blank=True, max_length=255)),
                ('rut', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
        migrations.CreateModel(
            name='InternationalTrader',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
                ('businessName', models.CharField(max_length=50, unique=True)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
        migrations.CreateModel(
            name='LocalTrader',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
                ('documentNumber', models.CharField(blank=True, max_length=255)),
                ('businessName', models.CharField(max_length=50, unique=True)),
                ('rut', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('useraccount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cuentas.useraccount')),
                ('documentNumber', models.CharField(blank=True, max_length=255)),
                ('businessName', models.CharField(max_length=50, unique=True)),
                ('rut', models.CharField(blank=True, max_length=255)),
                ('productType', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cuentas.useraccount',),
        ),
    ]
