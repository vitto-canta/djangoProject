# Generated by Django 2.2 on 2022-02-10 15:25

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
        ('product', '0001_initial'),
        ('costumer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('costumer_has_paid', models.BooleanField(default=False)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.PositiveIntegerField()),
                ('address_line_1', models.CharField(max_length=150)),
                ('address_line_2', models.CharField(blank=True, max_length=150)),
                ('town_city', models.CharField(max_length=150)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyers',
                                               to='costumer.Costumer')),
                ('vendors', models.ManyToManyField(related_name='sellers', to='vendor.Vendor')),
            ],
            options={
                'ordering': ['-created_at', 'paid_amount'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('vendor_paid', models.BooleanField(default=False)),
                ('is_shipped', models.BooleanField(default=False)),
                ('is_received', models.BooleanField(default=False)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer',
                                               to='costumer.Costumer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items',
                                            to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items',
                                              to='product.Product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller',
                                             to='vendor.Vendor')),
            ],
        ),
    ]
