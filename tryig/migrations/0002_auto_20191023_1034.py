# Generated by Django 2.2.2 on 2019-10-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.DeleteModel(
            name='tryadd',
        ),
    ]
