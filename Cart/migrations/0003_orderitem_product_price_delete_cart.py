# Generated by Django 4.2.5 on 2023-10-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_alter_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
