# Generated by Django 2.2.2 on 2019-06-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('GaurdainsName', models.CharField(max_length=30)),
                ('Occupation', models.CharField(max_length=30)),
                ('MailingAddress', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=20)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Hobbies', models.CharField(max_length=20)),
                ('LastInstitution', models.CharField(max_length=40)),
                ('Percentage', models.CharField(max_length=2)),
                ('Grade', models.CharField(max_length=2)),
                ('Players', models.CharField(max_length=30)),
            ],
        ),
    ]
