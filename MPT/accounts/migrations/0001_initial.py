# Generated by Django 4.0.3 on 2022-06-16 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('profile_img', models.ImageField(blank=True, default='logo.png', null=True, upload_to='images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_rollNo', models.IntegerField(null=True, unique=True)),
                ('AimForLife', models.CharField(blank=True, max_length=100, null=True)),
                ('reason_of_engg', models.CharField(blank=True, max_length=50, null=True)),
                ('semester', models.CharField(blank=True, max_length=50, null=True)),
                ('Course', models.CharField(blank=True, max_length=50, null=True)),
                ('YearOfAdmission', models.IntegerField(null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('DateofBirth', models.DateField(max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('Blood_grp', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=50, null=True)),
                ('Branch', models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Information Technology', 'Information Technology'), ('Mechanical Engineering', 'Mechanical Engineering')], max_length=70, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('State', models.CharField(max_length=50, null=True)),
                ('Country', models.CharField(max_length=50, null=True)),
                ('religion', models.CharField(max_length=50, null=True)),
                ('mother_tongue', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateofBirth', models.DateField(max_length=50, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('Blood_grp', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], max_length=50, null=True)),
                ('Branch', models.CharField(choices=[('Computer Engineering', 'Computer Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Information Technology', 'Information Technology'), ('Mechanical Engineering', 'Mechanical Engineering')], max_length=70, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('State', models.CharField(max_length=50, null=True)),
                ('Country', models.CharField(max_length=50, null=True)),
                ('religion', models.CharField(max_length=50, null=True)),
                ('mother_tongue', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('Mentee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.studentprofile')),
                ('Mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.mentorprofile')),
            ],
        ),
    ]
