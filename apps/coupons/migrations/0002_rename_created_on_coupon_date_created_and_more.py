# Generated by Django 5.1.2 on 2024-10-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='created_on',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='updated_on',
            new_name='date_modified',
        ),
    ]
