# Generated by Django 5.2 on 2025-04-03 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название породы')),
                ('description', models.TextField(verbose_name='Описание')),
                ('size', models.CharField(choices=[('small', 'Маленькая'), ('medium', 'Средняя'), ('large', 'Крупная')], max_length=10, verbose_name='Размер')),
                ('group', models.CharField(max_length=50, verbose_name='Группа')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('male', 'Кобель'), ('female', 'Сука')], max_length=10, verbose_name='Пол')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='dogs/', verbose_name='Фото')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.breed', verbose_name='Порода')),
            ],
        ),
    ]
