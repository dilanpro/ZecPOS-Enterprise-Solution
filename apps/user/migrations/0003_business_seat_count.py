# Generated by Django 5.0.1 on 2024-02-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_business_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='seat_count',
            field=models.IntegerField(default=1),
        ),
    ]
