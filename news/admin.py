from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from news.models import News, Category, Style, Categories

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(
    Categories,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)