# Generated by Django 5.0.1 on 2024-05-24 16:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_financesalesandinvoice_pdmaterialnolist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financesalesandinvoice',
            old_name='u9_no',
            new_name='material_no',
        ),
        migrations.RemoveField(
            model_name='financesalesandinvoice',
            name='invoice_time',
        ),
        migrations.RemoveField(
            model_name='financesalesandinvoice',
            name='num',
        ),
        migrations.RemoveField(
            model_name='financesalesandinvoice',
            name='price_with_tax',
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='invoice_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='已开票金额'),
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='invoice_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='已开票数量'),
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='post_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='邮费'),
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='refund_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='退款金额'),
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='sales_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='实际销售额'),
        ),
        migrations.AddField(
            model_name='financesalesandinvoice',
            name='sales_num',
            field=models.IntegerField(blank=True, null=True, verbose_name='实际销售量'),
        ),
        migrations.AlterField(
            model_name='financesalesandinvoice',
            name='goods_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='商品名称'),
        ),
        migrations.AlterField(
            model_name='financesalesandinvoice',
            name='goods_no',
            field=models.CharField(max_length=100, verbose_name='商家编码'),
        ),
        migrations.AlterField(
            model_name='financesalesandinvoice',
            name='shop_name',
            field=models.CharField(max_length=100, verbose_name='店铺名称'),
        ),
    ]
