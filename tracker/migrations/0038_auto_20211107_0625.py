# Generated by Django 3.1.7 on 2021-11-06 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0037_auto_20211107_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='relationship',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
    ]
