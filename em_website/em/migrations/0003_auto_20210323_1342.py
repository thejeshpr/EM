# Generated by Django 3.1.7 on 2021-03-23 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0002_auto_20210322_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='color',
            new_name='icon',
        ),
    ]
