# Generated by Django 5.0.1 on 2024-06-19 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_shopsalestarget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopsalestarget',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shoptarget', verbose_name='店铺'),
        ),
    ]
