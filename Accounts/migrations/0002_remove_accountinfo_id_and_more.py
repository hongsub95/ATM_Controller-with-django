# Generated by Django 4.1.3 on 2022-12-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='account_number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='계좌번호'),
        ),
    ]
