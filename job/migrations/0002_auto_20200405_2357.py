# Generated by Django 3.0.5 on 2020-04-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.CharField(default='', max_length=300, verbose_name='Изображение'),
        ),
    ]
