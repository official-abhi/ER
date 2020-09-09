# Generated by Django 3.0.7 on 2020-09-03 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('milkdairy', '0017_delete_user_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordersummery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('status', models.CharField(default='undelivered', max_length=20)),
                ('payment', models.CharField(default='unpaid', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milkdairy.Day')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milkdairy.Month')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='client.User_data')),
            ],
        ),
    ]
