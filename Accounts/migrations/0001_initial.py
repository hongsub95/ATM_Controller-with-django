# Generated by Django 4.1.3 on 2022-11-29 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='이름')),
                ('balance', models.BigIntegerField(verbose_name='잔액')),
                ('account_number', models.CharField(max_length=10, unique=True, verbose_name='계좌번호')),
                ('card_number', models.CharField(max_length=16, unique=True, verbose_name='카드번호')),
                ('pin', models.CharField(max_length=4, verbose_name='핀번호')),
                ('phone_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('010-?[1-9]\\d{3}-?\\d{4}$')], verbose_name='전화번호')),
            ],
        ),
    ]