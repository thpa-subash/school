# Generated by Django 2.2.2 on 2019-07-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mailaddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateo', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=1000)),
                ('body', models.TextField()),
            ],
        ),
    ]