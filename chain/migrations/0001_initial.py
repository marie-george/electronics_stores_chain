# Generated by Django 4.2.5 on 2023-10-02 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChainUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(max_length=150, verbose_name='страна')),
                ('city', models.CharField(max_length=150, verbose_name='город')),
                ('street', models.CharField(max_length=150, verbose_name='улица')),
                ('bld', models.CharField(max_length=150, verbose_name='номер дом')),
                ('debt', models.FloatField(default=0, verbose_name='задолженность перед поставщиком')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('hierarchy_level', models.CharField(choices=[('factory', 'завод'), ('retail_chain', 'розничная сеть'), ('ie', 'индивидуальный предприниматель')], verbose_name='уровень иерархии')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.chainunit', verbose_name='поставщик')),
            ],
        ),
    ]