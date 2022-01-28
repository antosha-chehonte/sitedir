from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from actual.models import Notes, Directions
from actual.forms import NoteEditForm, DirectionsEditForm
from django.contrib.auth.decorators import login_required


def actual_index(request, parent_id=1):
    direction = Directions.objects.filter(parent=parent_id, status=1)
    notes = Notes.objects.filter(direction_of_work=parent_id, status=1).order_by('-updated_at')
    # todo: предусмотреть выдачу только актуальных заметок (после добавления в модель)
    current_direction = Directions.objects.get(pk=parent_id)
    if not parent_id:
        parent = None
    else:
        parent_direction = Directions.objects.get(pk=parent_id)
        parent = parent_direction.parent

    context = {
        'direction': direction,
        'parent': parent,
        'notes': notes,
        'current_direction': current_direction,
    }

    return render(request, template_name="actual/actual_index.html", context=context)


def actual_directions_tree(request):
    directions = Directions.objects.all()
    context = {
        'nodes': directions,
    }

    return render(request, template_name="actual/directions_tree.html", context=context)


@login_required
def note_add(request, direction_id=1):
    revers_id = direction_id
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST)
        # todo: предусмотреть сохранение имени пользователя
        if post_form.is_valid():
            post_form.save()
            # return actual_index(request, parent_id=revers_id)
            # todo: настроить редирект на actual_index с текущим направлением деятельности
            return HttpResponseRedirect(reverse('actual_index'))
    else:
        post_form = NoteEditForm(initial={'direction_of_work': direction_id, 'status': 1})
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'actual/note_add.html', context)


@login_required
def note_edit(request, note_id):
    editable_note = Notes.objects.get(pk=note_id)
    revers_id = editable_note.direction_of_work.pk
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST, instance=editable_note)
        if post_form.is_valid():
            post_form.save()
            return actual_index(request, parent_id=revers_id)
    else:
        post_form = NoteEditForm(instance=editable_note)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
            "note_id": note_id,

        }
        return render(request, 'actual/note_edit.html', context)


@login_required
def directions_add(request, parent_id=1):
    revers_id = parent_id
    if request.method == 'POST':
        post_form = DirectionsEditForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('actual_index'))
    else:
        post_form = DirectionsEditForm(initial={'parent': parent_id, 'status': 1})
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'actual/directions_add.html', context)

@login_required
def directions_edit(request, direction_id):
    editable_direction = Directions.objects.get(pk=direction_id)
    revers_id = direction_id
    if request.method == 'POST':
        post_form = DirectionsEditForm(request.POST, instance=editable_direction)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('actual_index'))
    else:
        post_form = DirectionsEditForm(instance=editable_direction)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'actual/directions_edit.html', context)