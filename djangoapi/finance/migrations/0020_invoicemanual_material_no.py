# Generated by Django 5.0.1 on 2024-06-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0019_alter_douyinrefund_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicemanual',
            name='material_no',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='料号'),
        ),
    ]
