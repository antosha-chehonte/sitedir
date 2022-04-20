from django.urls import path
from it.views import it_index, it_note_add, it_note_edit, it_directions_tree

urlpatterns = [
    path('', it_index, name='it_index'),
    path('itdirections/<int:parent_id>', it_index, name='it_directions'),
    path('itdirections/tree', it_directions_tree, name='it_directions_tree'),
    # path('itadd/', it_note_add, name='it_note_add'),  # добавить заметку
    path('itaddid/<int:direction_id>', it_note_add, name='it_note_add_id'),  # добавить заметку по направлению
    path('itedit/<int:note_id>', it_note_edit, name='it_note_edit'),  # конкретная заметка
]
