# Generated by Django 5.0.1 on 2024-03-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_specgoods_goods_no_alter_specgoods_spec_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specgoods',
            name='allow_below_cost_price',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='允许低于成本价'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='aux_box_volume',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='辅助箱体积'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='prop2',
            field=models.TextField(blank=True, null=True, verbose_name='单品属性2'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='prop3',
            field=models.TextField(blank=True, null=True, verbose_name='单品属性3'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='prop4',
            field=models.TextField(blank=True, null=True, verbose_name='单品属性4'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='prop5',
            field=models.TextField(blank=True, null=True, verbose_name='单品属性5'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='prop6',
            field=models.TextField(blank=True, null=True, verbose_name='单品属性6'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='specgoods',
            name='u9_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='U9料号'),
        ),
        migrations.AddField(
            model_name='suitegoodsrec',
            name='img_url',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='图片链接'),
        ),
        migrations.AddField(
            model_name='suitegoodsrec',
            name='stock_num',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='库存'),
        ),
        migrations.AddField(
            model_name='suitegoodsrec',
            name='suite_barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='组合装条码'),
        ),
        migrations.AddField(
            model_name='suitegoodsrec',
            name='suite_no',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='组合装商家编码'),
        ),
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='spec_no',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='组合装明细商家编码'),
        ),
    ]
