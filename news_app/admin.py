from django.contrib import admin
from .models import Category, News
# Register your models here.

admin.site.site_header = 'Control Panel'

admin.site.register(Category)
admin.site.register(News)
