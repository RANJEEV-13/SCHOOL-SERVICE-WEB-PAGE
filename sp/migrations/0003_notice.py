# Generated by Django 3.0.5 on 2020-05-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0002_auto_20200517_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]