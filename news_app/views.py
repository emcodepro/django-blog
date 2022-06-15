from django.http import HttpResponseBadRequest
from django.shortcuts import render
from news_app.models import News, Category
from django.core.paginator import Paginator


# Create your views here.


def index(request):
  category_politic = Category.objects.get(name='Politic')
  category_culture = Category.objects.get(name='Culture')

  categories = Category.objects.all()
  top_five_news = News.objects.exclude(category_id__in=[category_politic.id, category_culture.id]).order_by('-id')[:5]

  latest_three_politic_news = category_politic.news.order_by('-id')[:3]
  latest_three_culture_news = category_culture.news.order_by('-id')[:3]

  articles = News.objects.order_by('-id')
  paginator = Paginator(articles, 12)

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  # four article after slider

  four_news = News.objects.exclude(category_id__in=[category_politic.id, category_culture.id]).order_by('-id')[5:][:4]

  four_news = {
    'first': four_news[0],
    'second': four_news[1],
    'three': four_news[2],
    'four': four_news[3],
  }

  return render(request, 'news_app/pages/index.html', {
    'categories': categories,
    'top_five_news': top_five_news,
    'latest_three_politic_news': latest_three_politic_news,
    'latest_three_culture_news': latest_three_culture_news,
    'page_obj': page_obj,
    'four_news': four_news
  })


def view(request, article_id):
  categories = Category.objects.all()
  article = News.objects.get(id=article_id)

  articles_in_this_category = categories.get(id=article.category.id).news.exclude(id=article.id).order_by('-id')[:6]

  return render(request, 'news_app/pages/view.html', {
    'article': article,
    'categories': categories,
    'articles_in_this_category': articles_in_this_category,
  })


def category(request, category_id):
  categories = Category.objects.all()
  cat = Category.objects.get(id=category_id)

  articles = cat.news.order_by('-id')
  paginator = Paginator(articles, 12)

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  return render(request, 'news_app/pages/category_view.html', {
    'page_obj': page_obj,
    'category': cat,
    'categories': categories,
  })


def search(request):
  keyword = request.GET.get('keyword')

  if not keyword:
    return HttpResponseBadRequest('Bad request')

  articles = News.objects.filter(title__contains=keyword, text__contains=keyword)
  paginator = Paginator(articles, 12)

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  return render(request, 'news_app/pages/category_view.html', {
    'page_obj': page_obj,
    'category': {
      'name': 'Search',
    },
  })


def contacts(request):
  return render(request, 'news_app/pages/contacts.html')
