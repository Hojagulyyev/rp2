# Generated by Django 4.2.6 on 2023-11-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
