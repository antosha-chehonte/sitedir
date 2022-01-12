from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from actual.models import Directions, Notes

# admin.site.register(DirectionsList)
admin.site.register(Notes)
admin.site.register(
    Directions,
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