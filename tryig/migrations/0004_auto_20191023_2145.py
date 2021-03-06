# Generated by Django 2.2.2 on 2019-10-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryig', '0003_auto_20191023_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='econtact',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ename',
        ),
        migrations.AddField(
            model_name='employee',
            name='FirstName',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='GaurdainsName',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='Gender',
            field=models.CharField(default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='Grade',
            field=models.CharField(default='one', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='Hobbies',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='LastInstitution',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AddField(
            model_name='employee',
            name='LastName',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='MailingAddress',
            field=models.CharField(default='Kathmandu', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='Occupation',
            field=models.CharField(default='Agricultural', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='Percentage',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='PhoneNumber',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='Players',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='Services',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='currentgrade',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emailid',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, default='/images/avatar.jpg', null=True, upload_to='images/profile/'),
        ),
        migrations.AlterModelTable(
            name='employee',
            table=None,
        ),
    ]
