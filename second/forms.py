from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import SecNotes, SecDirections


class SecNoteEditForm(forms.ModelForm):

    class Meta:
        model = SecNotes
        fields = [
            'note_title',
            'note_text',
            'direction_of_work',
            'status',
        ]
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-control'}),
            'note_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'direction_of_work': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class SecDirectionsEditForm(forms.ModelForm):

    class Meta:
        model = SecDirections
        fields = [
            'direction',
            'description',
            'parent',
            'status',
        ]
        widgets = {
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
