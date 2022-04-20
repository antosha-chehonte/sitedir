from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from second.models import SecNotes, SecDirections
from second.forms import SecNoteEditForm, SecDirectionsEditForm
from django.contrib.auth.decorators import login_required


def second_index(request, parent_id=1):
    direction = SecDirections.objects.filter(parent=parent_id, status=1)
    notes = SecNotes.objects.filter(direction_of_work=parent_id, status=1).order_by('-updated_at')
    # todo: предусмотреть выдачу только актуальных заметок (после добавления в модель)
    current_direction = SecDirections.objects.get(pk=parent_id)
    if not parent_id:
        parent = None
    else:
        parent_direction = SecDirections.objects.get(pk=parent_id)
        parent = parent_direction.parent

    context = {
        'direction': direction,
        'parent': parent,
        'notes': notes,
        'current_direction': current_direction,
    }

    return render(request, template_name="second/second_index.html", context=context)


def second_directions_tree(request):
    directions = SecDirections.objects.all()
    stat_directions_count = SecDirections.objects.filter(status=1).count()
    stat_note_count = SecNotes.objects.filter(status=1).count()
    stat_note_last = SecNotes.objects.filter(status=1).latest('updated_at')

    context = {
        'nodes': directions,
        'stat_note_count': stat_note_count,
        'stat_note_last': stat_note_last,
        'stat_directions_count': stat_directions_count,
    }

    return render(request, template_name="second/directions_tree.html", context=context)


@login_required
def second_note_add(request, direction_id=1):
    revers_id = direction_id
    if request.method == 'POST':
        post_form = SecNoteEditForm(request.POST)
        # todo: предусмотреть сохранение имени пользователя
        if post_form.is_valid():
            post_form.save()
            # return second_index(request, parent_id=revers_id)
            # todo: настроить редирект на second_index с текущим направлением деятельности
            return redirect('second_directions', parent_id=revers_id)
    else:
        post_form = SecNoteEditForm(initial={'direction_of_work': direction_id, 'status': 1})
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'second/note_add.html', context)


@login_required
def second_note_edit(request, note_id):
    editable_note = SecNotes.objects.get(pk=note_id)
    revers_id = editable_note.direction_of_work.pk
    if request.method == 'POST':
        post_form = SecNoteEditForm(request.POST, instance=editable_note)
        if post_form.is_valid():
            post_form.save()
            return redirect('second_directions', parent_id=revers_id)
    else:
        post_form = SecNoteEditForm(instance=editable_note)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
            "note_id": note_id,

        }
        return render(request, 'second/note_edit.html', context)


@login_required
def second_directions_add(request, parent_id=1):
    revers_id = parent_id
    if request.method == 'POST':
        post_form = SecDirectionsEditForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('second_index'))
    else:
        post_form = SecDirectionsEditForm(initial={'parent': parent_id, 'status': 1})
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'second/directions_add.html', context)


@login_required
def second_directions_edit(request, direction_id):
    editable_direction = SecDirections.objects.get(pk=direction_id)
    revers_id = direction_id
    if request.method == 'POST':
        post_form = SecDirectionsEditForm(request.POST, instance=editable_direction)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('second_index'))
    else:
        post_form = SecDirectionsEditForm(instance=editable_direction)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'second/directions_edit.html', context)

