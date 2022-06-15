from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view/<article_id>', views.view, name='view'),
    path('category/<category_id>', views.category, name='category'),
    path('search', views.search, name='search'),
    path('contacts', views.contacts, name='contacts')
]
