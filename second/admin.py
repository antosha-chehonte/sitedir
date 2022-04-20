from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from second.models import SecDirections, SecNotes, SecNoteStatus

# admin.site.register(DirectionsList)
admin.site.register(SecNotes)
admin.site.register(SecNoteStatus)
admin.site.register(
    SecDirections,
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