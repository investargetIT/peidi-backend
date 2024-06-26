# Generated by Django 5.0.1 on 2024-06-19 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_alter_stockdetail_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopSalesTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=40, verbose_name='时间')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=19, verbose_name='目标销售额')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shoptarget')),
            ],
            options={
                'verbose_name': '店铺销售目标',
                'verbose_name_plural': '店铺销售目标',
                'db_table': 'bi_shop_sales_target',
                'db_table_comment': '店铺销售目标',
            },
        ),
    ]
