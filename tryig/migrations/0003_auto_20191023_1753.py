# Generated by Django 2.2.2 on 2019-10-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tryig', '0002_auto_20191023_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='eemail',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='eid',
        ),
    ]
