# Generated by Django 5.0.3 on 2024-04-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
    ]