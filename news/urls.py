from django.urls import path
from news import views
from news.views import index, news

urlpatterns = [
    path('', index, name='index'),
    # todo: Remove this slash as it is unnecessary.
    #       If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
    path('/all/', news, name='news'),
    path('/category/<int:category_id>', views.news, name='news_category'),  # новости категории
    path('/<int:news_id>', views.news_view, name='news_view'),  # конкретная новость
    path('/edit/<int:news_id>', views.news_edit, name='news_edit'),  # конкретная новость
    path('/add/', views.news_add, name='add_news'),  # добавить новость
    # path('news/add-news-editor/', views.add_news_editor, name='add_news_editor'),  # добавить новость через редактор
    # path('logout/', views.logout, name='logout')
    # path('logout/', 'django.contrib.auth.views.logout', {'next_page': '/'})

]
