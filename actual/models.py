from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class DirectionsList(models.Model):
    direction_of_work = models.CharField(max_length=100, verbose_name='Направление работы')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание направления')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.direction_of_work

    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'
        ordering = ['direction_of_work']


class Notes(models.Model):
    note_title = models.CharField(max_length=100, verbose_name='Заголовок информации')
    note_text = RichTextUploadingField(blank=False, verbose_name='Содержание')
    direction_of_work = models.ForeignKey(DirectionsList, on_delete=models.PROTECT, verbose_name='Направление работы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return '%s - %s' % (self.direction_of_work, self.note_title)

    class Meta:
        verbose_name = 'Данные о состоянии законности'
        verbose_name_plural = 'Данные о состоянии законности'
        ordering = ['direction_of_work']
