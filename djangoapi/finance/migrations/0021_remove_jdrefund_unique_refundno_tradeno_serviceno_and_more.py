# Generated by Django 5.0.1 on 2024-06-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0020_invoicemanual_material_no'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='jdrefund',
            name='unique_refundno_tradeno_serviceno',
        ),
        migrations.AlterField(
            model_name='jdrefund',
            name='refund_no',
            field=models.CharField(max_length=100, unique=True, verbose_name='赔付单号'),
        ),
    ]
