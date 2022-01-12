from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Categories(MPTTModel):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование направления работы')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление работы (mptt)'
        verbose_name_plural = 'Направления работы (mptt)'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок объявления')
    content = RichTextUploadingField(blank=False, verbose_name='Содержание объявления')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # file = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Прикрепить файл', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    show_author = models.BooleanField(default=True, verbose_name='Показать автора объявления')
    pinned = models.BooleanField(default=False, verbose_name='Закрепить сообщение')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT,
                                 null=True, verbose_name='Направление деятельности')
    style = models.ForeignKey('Style', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Стиль оформления')

    # def filename(self):
    #     return os.path.basename(self.file.name)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_view', kwargs={"news_id": self.pk})

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование направления работы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'
        ordering = ['title']


class Style(models.Model):
    style = models.CharField(max_length=100, verbose_name='Стиль оформления')
    style_tag = models.CharField(max_length=100, verbose_name='Tag')

    def __str__(self):
        return self.style

    class Meta:
        verbose_name = 'Стиль оформления'
        verbose_name_plural = 'Стили оформления'
        ordering = ['style']


class Files(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True, verbose_name='Файл')
    contact = models.ForeignKey(News, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.file.name
