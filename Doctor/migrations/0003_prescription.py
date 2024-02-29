# Generated by Django 4.1.1 on 2022-10-22 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_alter_checkupdetails_checkup_result_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_medicine', models.TextField(null=True)),
                ('prescription_date', models.DateField(auto_now=True)),
                ('payment_status', models.IntegerField(default=0)),
                ('checkup_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctor.checkupdetails')),
            ],
        ),
    ]