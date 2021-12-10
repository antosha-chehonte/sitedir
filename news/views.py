from datetime import date

from django.contrib.auth import logout
# from django.core.paginator import Paginator
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.contrib.auth.decorators import login_required

# from news.forms import NewsEditForm
from news.models import News, Category


def get_ip(request):    # функция получения ip адреса пользователя
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    ip = get_ip(request)
    today = date.today()
    news_list = News.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day
    )
    news_list_yesterday = News.objects.filter(
        created_at__year=today.year,
        created_at__month=today.month,
        created_at__day=today.day-1
    )
    news_list_pinned = News.objects.filter(pinned=True)
    categories = Category.objects.all()
    # birthday = Employees.objects.filter(
    #     birthday__month=today.month,
    #     birthday__day=today.day,
    # )
    by_category = False
    # order_documents = OrderDocument.objects.all()
    context = {
        'news_list': news_list,
        'categories': categories,
        'by_category': by_category,
        'news_list_yesterday': news_list_yesterday,
        'news_list_pinned': news_list_pinned,
        # 'birthday': birthday,
        # 'order_documents': order_documents,
        'today': today,
        'ip': ip,
    }
    return render(request, template_name="news/index.html", context=context)


# def news(request, category_id=None):
#     if category_id:
#         news_list = News.objects.filter(category_id=category_id)
#         categories = Category.objects.all()
#         by_category = Category.objects.get(pk=category_id)
#         pinned_news = False
#     else:
#         news_list = News.objects.all()
#         categories = Category.objects.all()
#         by_category = False
#         pinned_news = True
#     paginator = Paginator(news_list, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'by_category': by_category,
#         'pinned_news': pinned_news,
#         'page_obj': page_obj
#     }
#     return render(request, template_name='news/news_all.html', context=context)


# def news_view(request, news_id):
#     news_list = News.objects.get(pk=news_id)
#     categories = Category.objects.all()
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#     }
#     return render(request, template_name='news/news_view.html', context=context)


# @login_required
# def news_add(request):
#     if request.method == 'POST':
#         post_form = NewsEditForm(request.POST)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect(index)
#     else:
#         post_form = NewsEditForm
#         context = {
#             "post_form": post_form,
#         }
#         return render(request, 'news/news_add.html', context)


# def news_edit(request, news_id):
#     editable_news = News.objects.get(pk=news_id)
#     editable = True
#     if request.method == 'POST':
#         post_form = NewsEditForm(request.POST, instance=editable_news)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect(index)
#     else:
#         post_form = NewsEditForm(instance=editable_news)
#         context = {
#             "post_form": post_form,
#             "editable": editable,
#         }
#         return render(request, 'news/news_add.html', context)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(to='/')
