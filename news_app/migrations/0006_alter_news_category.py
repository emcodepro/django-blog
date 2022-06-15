# Generated by Django 4.0.5 on 2022-06-14 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_news_image_alter_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news_app.category'),
        ),
    ]