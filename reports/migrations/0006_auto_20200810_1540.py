# Generated by Django 3.1 on 2020-08-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20200810_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cisbenchmark',
            name='check_id',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='check_id',
            field=models.FloatField(),
        ),
    ]
