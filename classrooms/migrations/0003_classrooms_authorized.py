# Generated by Django 3.0.6 on 2020-05-07 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classrooms', '0002_remove_classrooms_authorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrooms',
            name='authorized',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yetkili'),
            preserve_default=False,
        ),
    ]
