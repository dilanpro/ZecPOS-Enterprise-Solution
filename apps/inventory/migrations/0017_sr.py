# Generated by Django 5.0.1 on 2024-04-26 14:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_grnitem_quantity'),
        ('user', '0006_alter_user_business'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('special_note', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_finalized', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='srs', to='user.business')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='srs', to=settings.AUTH_USER_MODEL)),
                ('finalized_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finalized_srs', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='srs', to='inventory.supplier')),
            ],
        ),
    ]
