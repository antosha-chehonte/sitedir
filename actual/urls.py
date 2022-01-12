from django.urls import path
from actual.views import actual_index, note_add, note_edit, actual_directions_tree

urlpatterns = [
    path('', actual_index, name='actual_index'),
    path('directions/<int:parent_id>', actual_index, name='actual_directions'),
    path('directions/tree', actual_directions_tree, name='actual_directions_tree'),
    path('add/', note_add, name='note_add'),  # добавить заметку
    path('add/<int:direction_id>', note_add, name='note_add_id'),  # добавить заметку по конкретному направлению
    path('edit/<int:note_id>', note_edit, name='note_edit'),  # конкретная заметка
]
