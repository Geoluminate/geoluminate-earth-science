# Generated by Django 3.2.15 on 2022-08-23 16:23

from django.db import migrations
from ...utils import load_online_fixtures
from ..models import Plate


def forward(apps, schema_editor):
    load_online_fixtures(Plate.fixtures)


def reverse(apps, schema_editor):
    Plate.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]