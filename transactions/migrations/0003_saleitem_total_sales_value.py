# Generated by Django 3.0.7 on 2024-02-26 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20240214_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleitem',
            name='total_sales_value',
            field=models.IntegerField(default=0),
        ),
    ]