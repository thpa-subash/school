# Generated by Django 2.2.2 on 2019-08-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190809_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(default='static/img/avatar.jpg', upload_to='images/'),
        ),
    ]