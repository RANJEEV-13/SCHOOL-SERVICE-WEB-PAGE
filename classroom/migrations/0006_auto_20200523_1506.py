# Generated by Django 3.0.5 on 2020-05-23 09:36

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=djrichtextfield.models.RichTextField(verbose_name='questions'),
        ),
    ]
