# Generated by Django 4.0.5 on 2022-06-13 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_alter_news_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
