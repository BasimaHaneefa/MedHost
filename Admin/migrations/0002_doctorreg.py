# Generated by Django 4.1.1 on 2022-10-01 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('address', models.TextField(max_length=500, null=True)),
                ('gender', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='doctorphotos/')),
                ('experience', models.CharField(max_length=500)),
                ('doj', models.DateField(auto_now_add=True)),
                ('doctor_isactive', models.IntegerField(default=False)),
                ('password', models.CharField(max_length=50, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.department')),
            ],
        ),
    ]
