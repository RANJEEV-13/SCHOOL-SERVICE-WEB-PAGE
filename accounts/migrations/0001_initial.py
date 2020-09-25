# Generated by Django 3.0.5 on 2020-05-15 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tuition_Fee_Pay',
            fields=[
                ('feepayment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_month', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_enrolled', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('about_yourself', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('aadhar_number', models.CharField(blank=True, max_length=12, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('p_address', models.CharField(blank=True, max_length=200, null=True)),
                ('p_city', models.CharField(blank=True, max_length=100, null=True)),
                ('p_state', models.CharField(blank=True, max_length=100, null=True)),
                ('p_pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('c_address', models.CharField(blank=True, max_length=200, null=True)),
                ('c_city', models.CharField(blank=True, max_length=100, null=True)),
                ('c_state', models.CharField(blank=True, max_length=100, null=True)),
                ('c_pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('graduation_college', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_course', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_graduation', models.CharField(blank=True, max_length=10, null=True)),
                ('graduation_marksheet', models.FileField(blank=True, null=True, upload_to='graduation_marksheet')),
                ('senior_sec_name', models.CharField(blank=True, max_length=100, null=True)),
                ('senior_sec_stream', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_senior_sec', models.CharField(blank=True, max_length=10, null=True)),
                ('senior_sec_marksheet', models.FileField(blank=True, null=True, upload_to='senior_sec_marksheet')),
                ('secondary_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_secondary', models.CharField(blank=True, max_length=10, null=True)),
                ('secondary_marksheet', models.FileField(blank=True, null=True, upload_to='secondary_marksheet')),
                ('current_school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('current_school_marks', models.CharField(blank=True, max_length=10, null=True)),
                ('enrollment_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('contactno', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=100)),
                ('candidate_pic', models.ImageField(upload_to='candidate_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
