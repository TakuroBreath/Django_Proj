# Generated by Django 4.2.6 on 2024-01-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_changed_date_alter_product_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Is Published'),
        ),
    ]