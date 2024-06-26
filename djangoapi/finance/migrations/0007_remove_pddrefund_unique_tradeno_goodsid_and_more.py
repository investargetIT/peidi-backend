# Generated by Django 5.0.1 on 2024-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_invoice_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='pddrefund',
            name='unique_tradeno_goodsid',
        ),
        migrations.AddConstraint(
            model_name='pddrefund',
            constraint=models.UniqueConstraint(fields=('trade_no', 'goods_id', 'applicant'), name='unique_tradeno_goodsid_applicant'),
        ),
    ]
