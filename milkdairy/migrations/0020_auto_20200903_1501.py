# Generated by Django 3.0.7 on 2020-09-03 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_delete_deliveryboy'),
        ('milkdairy', '0019_ordersummery_hub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersummery',
            name='hub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.Hub_detail'),
        ),
    ]
