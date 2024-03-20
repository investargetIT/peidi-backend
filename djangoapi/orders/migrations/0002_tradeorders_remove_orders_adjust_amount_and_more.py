# Generated by Django 5.0.1 on 2024-03-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tradeOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(blank=True, max_length=40, null=True, verbose_name='原始单号')),
                ('oid', models.CharField(blank=True, max_length=40, null=True, verbose_name='原始子订单号')),
                ('status', models.CharField(blank=True, max_length=40, null=True, verbose_name='状态')),
                ('process_status', models.CharField(blank=True, max_length=40, null=True, verbose_name='处理状态')),
                ('refund_status', models.CharField(blank=True, max_length=40, null=True, verbose_name='退款状态')),
                ('order_type', models.CharField(blank=True, max_length=40, null=True, verbose_name='子订单类型')),
                ('goods_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='平台货品id')),
                ('spec_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='平台规格id')),
                ('goods_no', models.CharField(blank=True, max_length=40, null=True, verbose_name='货品编号')),
                ('spec_no', models.CharField(blank=True, max_length=40, null=True, verbose_name='规格编码')),
                ('goods_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='货品名称')),
                ('spec_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='规格名称')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='数量')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='单价')),
                ('adjust_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='调整')),
                ('discount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='优惠')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='总价')),
                ('share_discount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='分摊优惠')),
                ('share_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='分摊后应收')),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='退款金额')),
                ('refund_id', models.CharField(blank=True, max_length=40, null=True, verbose_name='退款单编号')),
                ('end_time', models.DateTimeField(blank=True, help_text='子单完成时间', null=True)),
                ('modified', models.DateTimeField(blank=True, help_text='修改时间', null=True)),
                ('created', models.DateTimeField(blank=True, help_text='创建时间', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='adjust_amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='created',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='goods_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='goods_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='goods_no',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='num',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='oid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_type',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='refund_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='share_amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='share_discount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='spec_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='spec_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='spec_no',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='orders',
            name='biaoqi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='标旗'),
        ),
        migrations.AddField(
            model_name='orders',
            name='buyer_message',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='买家备注'),
        ),
        migrations.AddField(
            model_name='orders',
            name='buyer_nick',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='客户网名'),
        ),
        migrations.AddField(
            model_name='orders',
            name='cash_on_delivery_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='货到付款金额'),
        ),
        migrations.AddField(
            model_name='orders',
            name='consumer_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='消费者实付金额'),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_term',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='货到付款'),
        ),
        migrations.AddField(
            model_name='orders',
            name='goods_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='货款'),
        ),
        migrations.AddField(
            model_name='orders',
            name='guarantee_mode',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='担保方式'),
        ),
        migrations.AddField(
            model_name='orders',
            name='other_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='其他收费'),
        ),
        migrations.AddField(
            model_name='orders',
            name='paid',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='已付'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pay_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='支付单号'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pay_method',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='支付方式'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pay_status',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='支付状态'),
        ),
        migrations.AddField(
            model_name='orders',
            name='pay_time',
            field=models.DateTimeField(blank=True, help_text='支付时间', null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='platform',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='平台'),
        ),
        migrations.AddField(
            model_name='orders',
            name='platform_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='平台承担优惠金额'),
        ),
        migrations.AddField(
            model_name='orders',
            name='platform_cost',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='平台费用'),
        ),
        migrations.AddField(
            model_name='orders',
            name='post_amount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='邮费'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receivable',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='应收'),
        ),
        migrations.AddField(
            model_name='orders',
            name='received',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='已收'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='收件人地址'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_area',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='省市县'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_mobile',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='收件人手机'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='收件人姓名'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_ring',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='区域（京东几环）'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_telno',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='收件人电话'),
        ),
        migrations.AddField(
            model_name='orders',
            name='receiver_zip',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='收件人邮编'),
        ),
        migrations.AddField(
            model_name='orders',
            name='remark',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='客服备注'),
        ),
        migrations.AddField(
            model_name='orders',
            name='shop_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='店铺'),
        ),
        migrations.AddField(
            model_name='orders',
            name='to_deliver_time',
            field=models.DateTimeField(blank=True, help_text='送货时间', null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='trade_status',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='平台状态'),
        ),
        migrations.AddField(
            model_name='orders',
            name='trade_time',
            field=models.DateTimeField(blank=True, help_text='下单时间', null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='warehouse_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='外部仓库编号'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='process_status',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='系统处理状态'),
        ),
    ]
