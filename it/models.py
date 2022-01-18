from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class ItDirections(MPTTModel):
    direction = models.CharField(max_length=100, verbose_name='Направление IT')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание IT направления')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.direction

    class MPTTMeta:
        order_insertion_by = ['direction']

    class Meta:
        verbose_name = 'Направление IT'
        verbose_name_plural = 'Направления IT работы'


class ItNotes(models.Model):
    note_title = models.CharField(max_length=100, verbose_name='Заголовок информации')
    note_text = RichTextUploadingField(blank=False, verbose_name='Содержание')
    direction_of_work = models.ForeignKey(ItDirections, on_delete=models.PROTECT, verbose_name='Направление работы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return '%s - %s' % (self.direction_of_work, self.note_title)

    class Meta:
        verbose_name = 'IT заметка'
        verbose_name_plural = 'IT заметки'
        ordering = ['direction_of_work']
