# Generated by Django 2.0 on 2017-12-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_historytimeline_bc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historytimeline',
            name='time',
            field=models.CharField(max_length=100, verbose_name='发生时间'),
        ),
    ]