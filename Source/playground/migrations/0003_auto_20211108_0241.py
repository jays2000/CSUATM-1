# Generated by Django 3.2.9 on 2021-11-08 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20211105_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='account_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='card_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.card'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='machine_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='playground.machine'),
        ),
    ]
