# Generated by Django 3.1.7 on 2021-04-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0009_transaction_pending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='pending',
        ),
        migrations.AlterField(
            model_name='account',
            name='icon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
