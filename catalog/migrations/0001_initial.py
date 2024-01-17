# Generated by Django 4.2.6 on 2024-01-17 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('description', models.TextField(blank='True', null='True', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(blank='True', null='True', verbose_name='Description')),
                ('image', models.ImageField(blank='True', null='True', upload_to='', verbose_name='Image')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('create_date', models.DateTimeField(verbose_name='Create Date')),
                ('changed_date', models.DateTimeField(verbose_name='Changed')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50, verbose_name='Version Number')),
                ('version_name', models.CharField(max_length=100, verbose_name='Name of version')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Version',
                'verbose_name_plural': 'Versions',
            },
        ),
    ]
