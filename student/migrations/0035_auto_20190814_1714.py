# Generated by Django 2.2.2 on 2019-08-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_auto_20190814_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(blank=True, default='images/avatar.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
