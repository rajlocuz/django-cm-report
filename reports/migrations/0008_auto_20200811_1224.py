# Generated by Django 3.1 on 2020-08-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20200810_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='prowleroutput',
            name='group',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prowleroutput',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prowleroutput',
            name='score',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prowleroutput',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='account_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='check_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='check_output',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='check_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prowleroutput',
            name='result',
            field=models.TextField(blank=True, null=True),
        ),
    ]
