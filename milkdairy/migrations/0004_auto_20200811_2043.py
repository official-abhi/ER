# Generated by Django 3.0.7 on 2020-08-11 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milkdairy', '0003_auto_20200811_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='hub_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='milkdairy.Hubs'),
        ),
    ]
