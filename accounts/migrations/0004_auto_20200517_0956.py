# Generated by Django 3.0.5 on 2020-05-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200517_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/default_profile_pic.png', null=True, upload_to='profile_pic'),
        ),
    ]
