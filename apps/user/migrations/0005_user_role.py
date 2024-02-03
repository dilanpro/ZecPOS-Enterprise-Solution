# Generated by Django 5.0.1 on 2024-02-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_onboading_date_business_onboarding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('AD', 'Admin'), ('MN', 'Manager'), ('CS', 'Cashier'), ('SK', 'Stock Keeper')], default='CS', max_length=2),
        ),
    ]
