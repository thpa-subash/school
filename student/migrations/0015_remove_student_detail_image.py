# Generated by Django 2.2.2 on 2019-08-09 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_auto_20190809_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_detail',
            name='image',
        ),
    ]
