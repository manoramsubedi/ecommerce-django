# Generated by Django 5.1 on 2024-08-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
