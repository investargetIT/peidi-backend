# Generated by Django 5.0.1 on 2024-05-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_tmallrefund_unique_tradeno_refundno_alipaytransactionno_goodsno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmallrefund',
            name='goods_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='宝贝标题'),
        ),
        migrations.AlterField(
            model_name='tmallrefund',
            name='goods_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='商品编码'),
        ),
    ]
