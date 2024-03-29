# Generated by Django 4.1.1 on 2022-10-17 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratory', '0001_initial'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkupdetails',
            name='checkup_result',
            field=models.FileField(default=0, upload_to='checkupresult/'),
        ),
        migrations.AlterField(
            model_name='checkupdetails',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratory.testdetails'),
        ),
    ]
