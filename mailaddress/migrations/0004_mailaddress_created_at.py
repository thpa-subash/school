# Generated by Django 2.2.2 on 2019-10-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailaddress', '0003_auto_20191029_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailaddress',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
