from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from actual.models import Notes, Directions
from actual.forms import NoteEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def actual_index(request, parent_id=1):
    direction = Directions.objects.filter(parent=parent_id)
    notes = Notes.objects.filter(direction_of_work=parent_id).order_by('-updated_at')
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
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('actual_index'))
    else:
        post_form = NoteEditForm(initial={'direction_of_work': direction_id})
        context = {
            "post_form": post_form,
        }
        return render(request, 'actual/note_add.html', context)


@login_required
def note_edit(request, note_id):
    editable_news = Notes.objects.get(pk=note_id)
    revers_id = editable_news.direction_of_work.pk
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST, instance=editable_news)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('actual_index'))
    else:
        post_form = NoteEditForm(instance=editable_news)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
            "note_id": note_id,

        }
        return render(request, 'actual/note_edit.html', context)
