from django.db import models

from config import settings


class ChainUnit(models.Model):
    """Модель объекта сети магазинов"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name='владелец')
    name = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    bld = models.CharField(max_length=150, verbose_name='номер дом')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=50, decimal_places=2, default=0, verbose_name='задолженность перед поставщиком')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    hierarchy_levels = (
        ('factory', 'завод'),
        ('retail_chain', 'розничная сеть'),
        ('ie', 'индивидуальный предприниматель')
    )
    hierarchy_level = models.CharField(choices=hierarchy_levels, verbose_name='уровень иерархии')

    class Meta:
        verbose_name = 'объект сети'
        verbose_name_plural = 'объекты сети'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=150, verbose_name='название')
    model_name = models.CharField(max_length=150, verbose_name='модель')
    issue_date = models.DateField(verbose_name='дата выхода на рынок')
    store = models.ForeignKey(ChainUnit, on_delete=models.CASCADE, blank=True, null=True, verbose_name='магазин')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

    def __str__(self):
        return self.name
