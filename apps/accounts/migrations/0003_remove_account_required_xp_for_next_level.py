# Generated by Django 4.2.6 on 2023-11-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_level_account_required_xp_for_next_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='required_xp_for_next_level',
        ),
    ]
