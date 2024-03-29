# Generated by Django 4.2.6 on 2024-01-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('preview', models.ImageField(blank='True', null='True', upload_to='', verbose_name='preview')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='created')),
                ('views', models.IntegerField(default=0, verbose_name='views')),
                ('is_published', models.BooleanField(default=True, verbose_name='published')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
