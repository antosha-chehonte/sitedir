from django.urls import path
from actual.views import actual_index, note_add

urlpatterns = [
    path('', actual_index, name='actual_index'),
    path('directions/<int:parent_id>', actual_index, name='actual_directions'),
    path('add/', note_add, name='note_add'),  # добавить заметку
]
