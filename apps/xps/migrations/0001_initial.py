# Generated by Django 4.2.6 on 2023-11-11 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_delete_xp'),
        ('diaries', '0003_diarycomment_created_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='XP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('earn_type', models.CharField(choices=[('diary_commit', 'Diary Commit')], max_length=64)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xps', to='accounts.account')),
                ('diary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='xps', to='diaries.diary')),
            ],
            options={
                'verbose_name': 'XP',
                'verbose_name_plural': 'XPs',
            },
        ),
    ]
