# Generated by Django 4.2.7 on 2024-01-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]