from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from it.models import ItDirections, ItNotes

# admin.site.register(DirectionsList)
admin.site.register(ItNotes)
admin.site.register(
    ItDirections,
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