# Generated by Django 2.2.7 on 2021-03-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_auto_20210317_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='alerttime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
