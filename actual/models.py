from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class NoteStatus(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус информации')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус информации'
        verbose_name_plural = 'Статусы информации'


class Directions(MPTTModel):
    direction = models.CharField(max_length=100, verbose_name='Направление работы')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание направления')
    status = models.ForeignKey(NoteStatus, on_delete=models.PROTECT, verbose_name='Статус направления')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Находится внутри направления',
        related_name='children')

    def __str__(self):
        return self.direction

    class MPTTMeta:
        order_insertion_by = ['direction']

    class Meta:
        verbose_name = 'Направление работы (mptt)'
        verbose_name_plural = 'Направления работы (mptt)'


class Notes(models.Model):
    note_title = models.CharField(max_length=100, verbose_name='Заголовок информации')
    note_text = RichTextUploadingField(blank=False, verbose_name='Содержание')
    direction_of_work = models.ForeignKey(Directions, on_delete=models.PROTECT, verbose_name='Направление работы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # todo: добавить поле с именем пользователя
    # todo: добавить поле статуса заметки (актуальна, удалена), отредактировать вью с учетом поля
    status = models.ForeignKey(NoteStatus, on_delete=models.PROTECT, verbose_name='Статус информации')

    def __str__(self):
        return '%s - %s' % (self.direction_of_work, self.note_title)

    class Meta:
        verbose_name = 'Данные о состоянии законности'
        verbose_name_plural = 'Данные о состоянии законности'
        ordering = ['direction_of_work']


# неиспользуемая модель
class DirectionsList(models.Model):
    direction_of_work = models.CharField(max_length=100, verbose_name='Направление работы')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание направления')
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.direction_of_work

    class Meta:
        verbose_name = 'Направление работы'
        verbose_name_plural = 'Направления работы'
        ordering = ['direction_of_work']
