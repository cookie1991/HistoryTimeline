# Generated by Django 2.0 on 2017-12-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20171221_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historytimeline',
            name='continent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='大洲'),
        ),
    ]
