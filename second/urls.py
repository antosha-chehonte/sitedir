from django.urls import path
from second.views import *

urlpatterns = [
    path('directions/', second_index, name='second_index'),
    path('directions/<int:parent_id>', second_index, name='second_directions'),
    path('directions/tree', second_directions_tree, name='second_directions_tree'),
    path('note_add/<int:direction_id>', second_note_add, name='second_note_add_id'),
    path('note_edit/<int:note_id>', second_note_edit, name='second_note_edit'),
    path('direction_add/<int:parent_id>', second_directions_add, name='second_directions_add'),
    path('direction_edit/<int:direction_id>', second_directions_edit, name='second_directions_edit'),
]
