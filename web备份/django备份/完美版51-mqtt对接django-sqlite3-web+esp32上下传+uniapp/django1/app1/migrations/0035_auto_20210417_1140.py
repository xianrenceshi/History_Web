# Generated by Django 2.2.7 on 2021-04-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_auto_20210417_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='air',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='airset',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='status',
            name='airstatus',
            field=models.IntegerField(default=0),
        ),
    ]
