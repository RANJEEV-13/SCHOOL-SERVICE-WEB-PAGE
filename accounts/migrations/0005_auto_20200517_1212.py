# Generated by Django 3.0.5 on 2020-05-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200517_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tuition_fee_pay',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='tuition_fee_pay',
            old_name='mobile',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='tuition_fee_pay',
            name='username',
        ),
        migrations.AddField(
            model_name='tuition_fee_pay',
            name='course_enrolled',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
