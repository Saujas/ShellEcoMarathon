# Generated by Django 2.0 on 2018-07-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180718_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
