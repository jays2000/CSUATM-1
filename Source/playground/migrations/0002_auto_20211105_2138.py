# Generated by Django 3.2.9 on 2021-11-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acc_num', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.AutoField(primary_key=True, serialize=False)),
                ('current_balance', models.FloatField()),
                ('location', models.TextField()),
                ('minimum_balance', models.FloatField()),
                ('last_refill', models.DateTimeField()),
                ('next_maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('Transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_num', models.IntegerField()),
                ('machine_id', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='card',
            name='id',
        ),
        migrations.AlterField(
            model_name='card',
            name='account_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]