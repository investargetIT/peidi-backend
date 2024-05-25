# Generated by Django 5.0.1 on 2024-05-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_shoptarget_shoptarget_shoptarget_unique_name_year'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='shoptarget',
            name='shoptarget_unique_name_year',
        ),
        migrations.AddField(
            model_name='shoptarget',
            name='dsr_date',
            field=models.DateField(blank=True, null=True, verbose_name='DSR日期'),
        ),
        migrations.AddField(
            model_name='shoptarget',
            name='logistic_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='物流体验分'),
        ),
        migrations.AddField(
            model_name='shoptarget',
            name='product_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='商品体验分'),
        ),
        migrations.AddField(
            model_name='shoptarget',
            name='service_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='服务体验分'),
        ),
    ]