# Generated by Django 3.0 on 2020-06-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecog', '0010_subincidents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subincidents',
            name='env',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='subincidents',
            name='inj',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='subincidents',
            name='pd',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='subincidents',
            name='veh',
            field=models.IntegerField(default=-1),
        ),
    ]