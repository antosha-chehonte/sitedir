from django.urls import path
from news import views
from news.views import index, news

urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('news/category/<int:category_id>', views.news, name='news_category'),  # новости категории
    path('news/<int:news_id>', views.news_view, name='news_view'),  # конкретная новость
    path('news/edit/<int:news_id>', views.news_edit, name='news_edit'),  # конкретная новость
    path('news/add-news/', views.news_add, name='add_news'),  # добавить новость
    # path('news/add-news-editor/', views.add_news_editor, name='add_news_editor'),  # добавить новость через редактор
    # path('logout/', views.logout, name='logout')
    # path('logout/', 'django.contrib.auth.views.logout', {'next_page': '/'})

]
