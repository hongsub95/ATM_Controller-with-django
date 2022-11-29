# Generated by Django 4.1.3 on 2022-11-29 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('account_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('balance', models.BigIntegerField(verbose_name='잔액')),
            ],
        ),
        migrations.RemoveField(
            model_name='cardinfo',
            name='balance',
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='account_number',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Accounts.accountinfo', verbose_name='계좌번호'),
        ),
    ]