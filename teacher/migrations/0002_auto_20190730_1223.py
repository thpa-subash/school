# Generated by Django 2.2.2 on 2019-07-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_detail',
            name='experience',
            field=models.CharField(default='none', max_length=2),
        ),
        migrations.AddField(
            model_name='teacher_detail',
            name='laststudyinstitution',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
