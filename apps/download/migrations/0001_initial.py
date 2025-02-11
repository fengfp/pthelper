# Generated by Django 4.1 on 2022-09-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='下载器名称')),
                ('typed', models.CharField(max_length=30, verbose_name='下载器类型tr,qb')),
                ('url', models.URLField(blank=True, verbose_name='下载器地址')),
                ('username', models.CharField(max_length=50, verbose_name='下载器用户名')),
                ('password', models.CharField(max_length=128, verbose_name='下载器密码')),
                ('dirname', models.CharField(max_length=150, null=True, verbose_name='默认下载目录')),
            ],
        ),
    ]
