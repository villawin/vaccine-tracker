# Generated by Django 3.1.7 on 2021-10-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20211018_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='landline',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
