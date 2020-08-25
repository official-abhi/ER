# Generated by Django 3.0.7 on 2020-08-12 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milkdairy', '0007_january'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.IntegerField()),
                ('next_month_id', models.IntegerField(blank=True, null=True)),
                ('next_day', models.IntegerField(blank=True, null=True)),
                ('next_year', models.CharField(blank=True, max_length=5, null=True)),
                ('members_id', models.ManyToManyField(to='milkdairy.Members')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(default='2020', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='January',
        ),
        migrations.AddField(
            model_name='day',
            name='month_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='milkdairy.Month'),
        ),
    ]
