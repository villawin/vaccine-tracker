# Generated by Django 3.2.4 on 2021-11-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0028_auto_20211101_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]