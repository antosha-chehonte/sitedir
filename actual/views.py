from django.shortcuts import render, redirect
from actual.models import DirectionsList, Notes
from actual.forms import NoteEditForm
from django.contrib.auth.decorators import login_required


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


@login_required
def note_add(request):
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            # return redirect(note_add)
            return render(request, 'actual/note_add.html')
    else:
        post_form = NoteEditForm
        context = {
            "post_form": post_form,
        }
        return render(request, 'actual/note_add.html', context)


@login_required
def note_edit(request, note_id):
    editable_news = Notes.objects.get(pk=note_id)
    editable = True
    revers_id = editable_news.direction_of_work.pk
    if request.method == 'POST':
        post_form = NoteEditForm(request.POST, instance=editable_news)
        if post_form.is_valid():
            post_form.save()
            # return redirect(index)
    else:
        post_form = NoteEditForm(instance=editable_news)
        context = {
            "post_form": post_form,
            "editable": editable,
            "revers_id": revers_id,

        }
        return render(request, 'actual/note_add.html', context)