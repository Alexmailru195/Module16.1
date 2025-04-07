from django.db import models

# Create your models here.

from django.db import models


class Breed(models.Model):
    SIZE_CHOICES = [
        ('small', 'Маленькая'),
        ('medium', 'Средняя'),
        ('large', 'Крупная'),
    ]

    name = models.CharField('Название породы', max_length=100)
    description = models.TextField('Описание')
    size = models.CharField('Размер', max_length=10, choices=SIZE_CHOICES)
    group = models.CharField('Группа', max_length=50)

    def __str__(self):
        return self.name


class Dog(models.Model):
    GENDER_CHOICES = [
        ('male', 'Кобель'),
        ('female', 'Сука'),
    ]

    name = models.CharField('Кличка', max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    age = models.PositiveIntegerField('Возраст')
    gender = models.CharField('Пол', max_length=10, choices=GENDER_CHOICES)
    description = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='dogs/')

    def __str__(self):
        return f"{self.name} ({self.breed})"
