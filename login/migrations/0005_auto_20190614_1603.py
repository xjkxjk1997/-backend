# Generated by Django 2.2.2 on 2019-06-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20190614_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.IntegerField(default='1'),
        ),
    ]
