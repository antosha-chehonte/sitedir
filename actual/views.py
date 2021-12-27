from django.shortcuts import render
from actual.models import DirectionsList, Notes


def actual_index(request, parent_id=1):
    direction = DirectionsList.objects.filter(parent=parent_id)
    notes = Notes.objects.filter(direction_of_work=parent_id).order_by('-updated_at')
    current_direction = DirectionsList.objects.get(pk=parent_id)
    if not parent_id:
        parent = None
    else:
        parent_direction = DirectionsList.objects.get(pk=parent_id)
        parent = parent_direction.parent

    context = {
        'direction': direction,
        'parent': parent,
        'notes': notes,
        'current_direction': current_direction,
    }

    return render(request, template_name="actual/actual_index.html", context=context)
