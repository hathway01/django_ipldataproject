# Generated by Django 2.1.1 on 2018-10-02 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20181002_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='match_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Matches'),
        ),
    ]