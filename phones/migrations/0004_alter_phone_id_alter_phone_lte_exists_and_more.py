# Generated by Django 4.2.4 on 2023-08-26 15:20

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.TextField(verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(verbose_name='Дата релиза'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
