# Generated by Django 3.0 on 2020-06-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecog', '0008_auto_20200607_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='dtinc',
            field=models.CharField(max_length=256),
        ),
    ]
