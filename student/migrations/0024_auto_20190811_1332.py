# Generated by Django 2.2.2 on 2019-08-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20190811_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
