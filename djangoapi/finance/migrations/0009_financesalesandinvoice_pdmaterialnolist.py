# Generated by Django 5.0.1 on 2024-05-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_goodssalessummary_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceSalesAndInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_time', models.DateTimeField(verbose_name='日期')),
                ('shop_name', models.CharField(max_length=100, verbose_name='订货客户')),
                ('goods_no', models.CharField(max_length=100, verbose_name='货号')),
                ('u9_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='料号')),
                ('goods_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='品名')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='数量')),
                ('price_with_tax', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='价税合计')),
            ],
        ),
        migrations.CreateModel(
            name='PDMaterialNOList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='采购分类.分类名称')),
                ('material_no', models.CharField(max_length=100, unique=True, verbose_name='料号')),
                ('goods_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='品名')),
                ('invoice_goods_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='开票品名')),
                ('goods_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='货号')),
                ('no_product_series', models.CharField(blank=True, max_length=100, null=True, verbose_name='重编编号(产品系列)')),
                ('barcode', models.CharField(blank=True, max_length=100, null=True, verbose_name='条码')),
                ('unit', models.CharField(blank=True, max_length=40, null=True, verbose_name='库存单位.名称')),
                ('feature', models.CharField(blank=True, max_length=40, null=True, verbose_name='料品形态属性')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='品牌')),
                ('weight', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='(单件重)')),
            ],
        ),
    ]
