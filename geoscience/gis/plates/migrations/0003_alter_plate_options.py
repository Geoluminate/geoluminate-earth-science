# Generated by Django 3.2.16 on 2022-12-30 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0002_load_fixtures'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plate',
            options={'verbose_name': 'Tectonic Plate', 'verbose_name_plural': 'Tectonic Plates'},
        ),
    ]