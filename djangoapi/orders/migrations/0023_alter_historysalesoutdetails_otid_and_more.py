# Generated by Django 5.0.1 on 2024-04-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_historysalesoutdetails_otid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historysalesoutdetails',
            name='otid',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='子单原始单号'),
        ),
        migrations.AlterField(
            model_name='historysalesoutdetails',
            name='tid',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='原始单号'),
        ),
    ]
