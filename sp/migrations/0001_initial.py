# Generated by Django 3.0.5 on 2020-05-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contactno', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('resume', models.FileField(upload_to='resume')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=100)),
                ('Course_Teacher_Name', models.CharField(max_length=100)),
                ('Seat', models.IntegerField()),
                ('Course_Duration', models.IntegerField()),
                ('Course_Description', models.TextField()),
                ('Course_Image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_link_name', models.CharField(max_length=100)),
                ('upload_file', models.FileField(upload_to='downloads')),
                ('file_download_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=100)),
                ('Teacher_Designation', models.CharField(max_length=50)),
                ('Teacher_Description', models.CharField(max_length=100)),
                ('Teacher_Image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
