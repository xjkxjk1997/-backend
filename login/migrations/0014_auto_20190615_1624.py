# Generated by Django 2.2.2 on 2019-06-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_transaction_accepter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='accepter',
            new_name='acceptor',
        ),
    ]
