# Generated by Django 3.0.5 on 2020-05-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloads',
            name='file_download_name',
            field=models.CharField(max_length=500),
        ),
    ]