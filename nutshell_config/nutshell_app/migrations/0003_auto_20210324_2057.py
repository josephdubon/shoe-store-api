# Generated by Django 3.1.7 on 2021-03-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutshell_app', '0002_auto_20210324_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsmanufacturer',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nsshoe',
            name='brand_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='nsshoe',
            name='fasten_type',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='nsshoe',
            name='material',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='nsshoe',
            name='size',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='nsshoetype',
            name='style',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
