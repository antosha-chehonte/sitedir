# Generated by Django 3.2.9 on 2021-12-03 19:03

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Наименование направления работы')),
            ],
            options={
                'verbose_name': 'Направление работы',
                'verbose_name_plural': 'Направления работы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=100, verbose_name='Стиль оформления')),
                ('style_tag', models.CharField(max_length=100, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Стиль оформления',
                'verbose_name_plural': 'Стили оформления',
                'ordering': ['style'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок объявления')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание объявления')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('show_author', models.BooleanField(default=True, verbose_name='Показать автора объявления')),
                ('pinned', models.BooleanField(default=False, verbose_name='Закрепить сообщение')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Направление деятельности')),
                ('style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.style', verbose_name='Стиль оформления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/', verbose_name='Файл')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news')),
            ],
            options={
                'verbose_name': 'Файлы',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
