# Generated by Django 4.1 on 2022-09-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0004_remove_config_refresh_time_rule_refresh_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='crontab_id',
            field=models.CharField(max_length=64, null=True, verbose_name='执行ID'),
        ),
    ]
