# Generated by Django 4.2.5 on 2023-10-02 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0003_alter_chainunit_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainunit',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.chainunit', verbose_name='поставщик'),
        ),
    ]