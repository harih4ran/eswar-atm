# Generated by Django 4.1.2 on 2022-10-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_pincode_account_pin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(blank=True, choices=[('CURRENT', 'CURRENT'), ('SAVINGS', 'SAVINGS')], max_length=40, null=True),
        ),
    ]
