# Generated by Django 5.0.1 on 2024-03-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_rename_cost_grnitem_actual_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='grnitem',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]