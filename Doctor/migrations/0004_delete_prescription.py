# Generated by Django 4.1.2 on 2022-10-26 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_prescription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]