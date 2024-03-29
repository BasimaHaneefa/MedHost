# Generated by Django 4.1.2 on 2022-10-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_userregistration_address'),
        ('Admin', '0006_slots'),
        ('User', '0004_delete_appoinment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_date', models.DateField(auto_now=True)),
                ('for_date', models.DateField()),
                ('appoinment_time', models.TimeField()),
                ('status', models.IntegerField(default=0)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.userregistration')),
                ('slot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.slots')),
            ],
        ),
    ]
