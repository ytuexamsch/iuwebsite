# Generated by Django 3.0.6 on 2020-05-07 21:02

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
                ('classroom_code', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Sınıf Kodu')),
                ('classroom_name', models.CharField(max_length=25, verbose_name='Sınıf Adı')),
                ('classroom_capacity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Sınıf Kapasitesi')),
                ('lab_or_not', models.CharField(choices=[('1', 'Laboratuvar Sınıfı'), ('0', 'Normal Sınıf')], max_length=20, verbose_name='Laboratuvar Sınıfı Mı?')),
                ('authorized', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yetkili')),
            ],
        ),
    ]
