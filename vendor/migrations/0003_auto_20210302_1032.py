# Generated by Django 3.1.7 on 2021-03-02 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20210302_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='551f15c9-b', max_length=150),
        ),
    ]
