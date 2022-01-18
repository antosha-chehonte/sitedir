from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import ItNotes


class ItNoteEditForm(forms.ModelForm):

    class Meta:
        model = ItNotes
        fields = [
            'note_title',
            'note_text',
            'direction_of_work',
        ]
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-control'}),
            'note_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'direction_of_work': forms.Select(attrs={'class': 'form-control'}),
        }
