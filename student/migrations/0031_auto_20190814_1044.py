# Generated by Django 2.2.2 on 2019-08-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0030_auto_20190813_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='image',
            field=models.ImageField(blank=True, default='images/avatar.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
