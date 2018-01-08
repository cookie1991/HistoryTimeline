# Generated by Django 2.0 on 2017-12-22 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_auto_20171222_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(max_length=10, verbose_name='大洲')),
            ],
        ),
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='国家')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.ContinentModel')),
            ],
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('birthday', models.CharField(blank=True, max_length=100, null=True, verbose_name='出生日期')),
                ('death', models.CharField(blank=True, max_length=100, null=True, verbose_name='去世日期')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='出生地')),
                ('abstract', models.CharField(max_length=100, verbose_name='人物简介')),
                ('detailed', models.TextField(verbose_name='人物介绍')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='timeline.CountryModel')),
            ],
        ),
        migrations.RemoveField(
            model_name='historytimeline',
            name='continent',
        ),
        migrations.AlterField(
            model_name='historytimeline',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.CountryModel'),
        ),
    ]