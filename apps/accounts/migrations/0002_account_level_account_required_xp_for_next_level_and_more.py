# Generated by Django 4.2.6 on 2023-11-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='account',
            name='required_xp_for_next_level',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='account',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
