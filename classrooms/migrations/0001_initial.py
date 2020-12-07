# Generated by Django 3.1.4 on 2020-12-07 18:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_code', models.CharField(max_length=3, verbose_name='Classroom Code')),
                ('classroom_name', models.CharField(max_length=25, verbose_name='Classroom Name')),
                ('classroom_capacity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Classroom Capacity')),
                ('lab_or_not', models.CharField(choices=[('1', 'Lab Classroom'), ('0', 'Standard Classroom')], max_length=20, verbose_name='Lab or Not')),
                ('authorized', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Authorized')),
            ],
        ),
    ]