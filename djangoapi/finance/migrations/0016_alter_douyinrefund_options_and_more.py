# Generated by Django 5.0.1 on 2024-06-12 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0015_rename_refund_apply_time_tmallrefund_apply_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='douyinrefund',
            options={'verbose_name': '抖音仅退款', 'verbose_name_plural': '抖音仅退款'},
        ),
        migrations.AlterModelOptions(
            name='goodssalessummary',
            options={'verbose_name': '旺店通货品销售汇总表', 'verbose_name_plural': '旺店通货品销售汇总表'},
        ),
        migrations.AlterModelOptions(
            name='invoice',
            options={'verbose_name': '发票', 'verbose_name_plural': '发票'},
        ),
        migrations.AlterModelOptions(
            name='jdrefund',
            options={'verbose_name': '京东仅退款', 'verbose_name_plural': '京东仅退款'},
        ),
        migrations.AlterModelOptions(
            name='pddrefund',
            options={'verbose_name': '拼多多仅退款', 'verbose_name_plural': '拼多多仅退款'},
        ),
        migrations.AlterModelOptions(
            name='pdmaterialnolist',
            options={'verbose_name': '智创料号清单', 'verbose_name_plural': '智创料号清单'},
        ),
        migrations.AlterModelOptions(
            name='tmallrefund',
            options={'verbose_name': '天猫仅退款', 'verbose_name_plural': '天猫仅退款'},
        ),
    ]
