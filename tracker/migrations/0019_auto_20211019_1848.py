# Generated by Django 3.1.7 on 2021-10-19 10:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0018_auto_20211019_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='ccontact',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='cfull_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='relation',
        ),
        migrations.AddField(
            model_name='patient',
            name='c1contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='c1full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='c2contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='c2full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='relation1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='relation2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
