# Generated by Django 3.0.8 on 2020-07-20 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0009_auto_20200720_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.Test', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='test',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='test',
            name='passed_quantity',
            field=models.IntegerField(default=0, verbose_name='Количество прошедших'),
        ),
    ]