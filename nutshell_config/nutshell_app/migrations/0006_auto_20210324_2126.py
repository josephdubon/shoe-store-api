# Generated by Django 3.1.7 on 2021-03-24 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutshell_app', '0005_auto_20210324_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsshoe',
            name='manufacturer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='nutshell_app.nsmanufacturer'),
        ),
    ]