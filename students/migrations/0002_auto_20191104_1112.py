# Generated by Django 2.2.2 on 2019-11-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeadd',
            name='payment',
            field=models.IntegerField(default=0),
        ),
    ]
