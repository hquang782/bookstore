# Generated by Django 4.1.13 on 2024-01-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(help_text='Unique value for category page URL, created from name.', unique=True)),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta Description')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['-created_at'],
            },
        ),
    ]