from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from it.models import ItNotes, ItDirections
from it.forms import ItNoteEditForm
from django.contrib.auth.decorators import login_required


def it_index(request, parent_id=1):
    direction = ItDirections.objects.filter(parent=parent_id)
    notes = ItNotes.objects.filter(direction_of_work=parent_id).order_by('-updated_at')
    current_direction = ItDirections.objects.get(pk=parent_id)
    if not parent_id:
        parent = None
    else:
        parent_direction = ItDirections.objects.get(pk=parent_id)
        parent = parent_direction.parent

    context = {
        'direction': direction,
        'parent': parent,
        'notes': notes,
        'current_direction': current_direction,
    }

    return render(request, template_name="it/it_index.html", context=context)


def it_directions_tree(request):
    directions = ItDirections.objects.all()
    context = {
        'nodes': directions,
    }

    return render(request, template_name="it/it_directions_tree.html", context=context)


@login_required
def it_note_add(request, direction_id=1):
    revers_id = direction_id
    if request.method == 'POST':
        post_form = ItNoteEditForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('it_index'))
    else:
        post_form = ItNoteEditForm(initial={'direction_of_work': direction_id})
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
        }
        return render(request, 'it/it_note_add.html', context)


@login_required
def it_note_edit(request, note_id):
    editable_news = ItNotes.objects.get(pk=note_id)
    revers_id = editable_news.direction_of_work.pk
    if request.method == 'POST':
        post_form = ItNoteEditForm(request.POST, instance=editable_news)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse('it_index'))
    else:
        post_form = ItNoteEditForm(instance=editable_news)
        context = {
            "post_form": post_form,
            "revers_id": revers_id,
            "note_id": note_id,

        }
        return render(request, 'it/it_note_edit.html', context)
