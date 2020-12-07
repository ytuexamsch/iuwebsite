# Generated by Django 3.0.6 on 2020-05-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0003_classrooms_authorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrooms',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='classroom_code',
            field=models.CharField(max_length=3, verbose_name='Sınıf Kodu'),
        ),
    ]
