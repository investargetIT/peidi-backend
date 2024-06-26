# Generated by Django 5.0.1 on 2024-06-19 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_alter_shopsalestarget_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopsalestarget',
            name='time',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(message='年度目标时间格式为YYYY，月度目标时间例如YYYY-MM', regex='^\\d{4}(-\\d{2})?$')], verbose_name='目标时间'),
        ),
        migrations.AddConstraint(
            model_name='shopsalestarget',
            constraint=models.UniqueConstraint(fields=('time', 'shop'), name='unique_time_shop'),
        ),
    ]