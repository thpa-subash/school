# Generated by Django 2.2.2 on 2019-08-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190809_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(default='pics/images/avatar.jpg', upload_to='images/'),
        ),
    ]
