# Generated by Django 2.2.2 on 2019-08-02 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailaddress', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailaddress',
            old_name='cateo',
            new_name='to',
        ),
    ]