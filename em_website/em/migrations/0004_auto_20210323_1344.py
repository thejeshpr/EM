# Generated by Django 3.1.7 on 2021-03-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0003_auto_20210323_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, default='las la-question-circle', max_length=20, null=True),
        ),
    ]
