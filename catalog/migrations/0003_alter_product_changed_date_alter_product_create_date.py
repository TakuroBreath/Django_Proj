# Generated by Django 4.2.6 on 2024-01-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='changed_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Changed'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Date'),
        ),
    ]