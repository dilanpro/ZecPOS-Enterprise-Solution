# Generated by Django 5.0.1 on 2024-03-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_grn_finalized_by_grnitem_finalized_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='grnitem',
            name='quantity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
