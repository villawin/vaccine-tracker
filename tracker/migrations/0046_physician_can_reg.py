# Generated by Django 3.2.4 on 2021-11-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0045_physician_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='can_reg',
            field=models.BooleanField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], null=True),
        ),
    ]
