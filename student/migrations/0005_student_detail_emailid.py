# Generated by Django 2.2.2 on 2019-07-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190726_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_detail',
            name='emailid',
            field=models.CharField(default='none', max_length=20),
        ),
    ]