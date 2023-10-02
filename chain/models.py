from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class ChainUnit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name='владелец')
    name = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    bld = models.CharField(max_length=150, verbose_name='номер дом')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='поставщик')
    debt = models.FloatField(default=0, verbose_name='задолженность перед поставщиком')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    hierarchy_levels = (
        ('factory', 'завод'),
        ('retail_chain', 'розничная сеть'),
        ('ie', 'индивидуальный предприниматель')
    )
    hierarchy_level = models.CharField(choices=hierarchy_levels, verbose_name='уровень иерархии')
