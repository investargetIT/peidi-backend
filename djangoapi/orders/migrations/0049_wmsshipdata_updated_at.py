# Generated by Django 5.0.1 on 2024-08-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0048_salesoutdetails_orders_sale_trade_n_5ebba6_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmsshipdata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
