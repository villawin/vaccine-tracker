# Generated by Django 3.1.7 on 2021-11-29 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0050_auto_20211130_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.patient'),
        ),
    ]
