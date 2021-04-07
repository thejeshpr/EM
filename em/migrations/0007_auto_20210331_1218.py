# Generated by Django 3.1.7 on 2021-03-31 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('em', '0006_keystore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('icon', models.CharField(max_length=200)),
                ('typ', models.CharField(choices=[('S', 'Savings'), ('C', 'Credit')], max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='accout',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='em.account'),
        ),
    ]
