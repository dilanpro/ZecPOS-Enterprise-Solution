# Generated by Django 5.0.1 on 2024-03-20 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_rename_price_grnitem_item_price_remove_grnitem_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grnitem',
            old_name='cost',
            new_name='actual_cost',
        ),
    ]
