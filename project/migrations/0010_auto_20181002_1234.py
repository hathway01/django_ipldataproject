# Generated by Django 2.1.1 on 2018-10-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_deliveries_match_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='match_id',
            field=models.IntegerField(null=True),
        ),
    ]
