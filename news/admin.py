from django.contrib import admin
from news.models import News, Category, Style

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Style)
