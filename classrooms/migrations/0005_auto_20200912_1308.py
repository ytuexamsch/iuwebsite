# Generated by Django 2.2.10 on 2020-09-12 10:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0004_auto_20200508_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrooms',
            name='authorized',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Authorized'),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='classroom_capacity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Classroom Capacity'),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='classroom_code',
            field=models.CharField(max_length=3, verbose_name='Classroom Code'),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='classroom_name',
            field=models.CharField(max_length=25, verbose_name='Classroom Name'),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='lab_or_not',
            field=models.CharField(choices=[('1', 'Lab Classroom'), ('0', 'Standard Classroom')], max_length=20, verbose_name='Lab or Not'),
        ),
    ]
