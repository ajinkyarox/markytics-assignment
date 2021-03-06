# Generated by Django 3.0 on 2020-06-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecog', '0007_auto_20200530_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=256)),
                ('indes', models.CharField(max_length=256)),
                ('dtinc', models.DateTimeField()),
                ('incloc', models.CharField(max_length=256)),
                ('insev', models.CharField(max_length=256)),
                ('suscau', models.CharField(max_length=256)),
                ('imactk', models.CharField(max_length=256)),
                ('repby', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'Form',
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='lid',
        ),
        migrations.DeleteModel(
            name='LoginCredentials',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
