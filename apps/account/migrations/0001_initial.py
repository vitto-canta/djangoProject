# Generated by Django 2.2 on 2022-02-10 15:25

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('surname', models.CharField(blank=True, max_length=150)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('postcode', models.CharField(blank=True, max_length=12)),
                ('address_line_1', models.CharField(blank=True, max_length=150)),
                ('address_line_2', models.CharField(blank=True, max_length=150)),
                ('town_city', models.CharField(blank=True, max_length=150)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_costumer', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Accounts',
                'verbose_name_plural': 'Accounts',
                'ordering': ['-last_login', 'username'],
            },
        ),
    ]
