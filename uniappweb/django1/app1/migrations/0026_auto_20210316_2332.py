# Generated by Django 2.2.7 on 2021-03-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20210316_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='settime',
            field=models.FloatField(default=0.0),
        ),
    ]
