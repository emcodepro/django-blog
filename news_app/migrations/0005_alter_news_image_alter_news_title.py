# Generated by Django 4.0.5 on 2022-06-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=1024),
        ),
    ]
