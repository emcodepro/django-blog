from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
    return f'{self.name}'

  class Meta:
    db_table = 'categories'
    verbose_name_plural = 'Categories'


class News(models.Model):
  title = models.CharField(max_length=1024)
  text = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
  image = models.ImageField()

  def __str__(self):
    return f'{self.title}'

  def get_image_url(self):
    return f'{settings.STATIC_URL}images/uploads/{self.image}'

  class Meta:
    db_table = 'news'
    verbose_name_plural = 'News'
