# Generated by Django 4.1.7 on 2023-04-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='main_pages.service', verbose_name='Услуги'),
        ),
    ]