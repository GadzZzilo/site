# Generated by Django 4.1.7 on 2023-03-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.PositiveIntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='human',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='human',
            name='description',
            field=models.TextField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='human',
            name='married',
            field=models.BooleanField(verbose_name='Женат/Замужем'),
        ),
        migrations.AlterField(
            model_name='human',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='human',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='human',
            name='work',
            field=models.CharField(max_length=100, verbose_name='Место работы'),
        ),
    ]
