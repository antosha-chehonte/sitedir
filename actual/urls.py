from django.urls import path
from actual.views import *

urlpatterns = [
    path('', redirect_to_actual, name='redirect_to_actual'),
    path('directions/', actual_index, name='actual_index'),
    path('directions/<int:parent_id>', actual_index, name='actual_directions'),
    path('directions/tree', actual_directions_tree, name='actual_directions_tree'),
    # path('note_add/', note_add, name='note_add'),  # добавить заметку
    path('note_add/<int:direction_id>', note_add, name='note_add_id'),  # добавить заметку по конкретному направлению
    path('note_edit/<int:note_id>', note_edit, name='note_edit'),  # конкретная заметка
    path('direction_add/<int:parent_id>', directions_add, name='directions_add'),  # добавить направление
    path('direction_edit/<int:direction_id>', directions_edit, name='directions_edit'),  # изменить направление

]
