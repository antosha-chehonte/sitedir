from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import News


class NewsEditForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget, label='')

    class Meta:
        model = News
        fields = [
            'category',
            'title',
            'content',
            'style',
            'status',
            'pinned',
            'author',
            'show_author',
            'is_published',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'style': forms.Select(attrs={'class': 'form-select', 'style': 'width:460px'}),
            'status': forms.Select(attrs={'class': 'form-select', 'style': 'width:460px'}),
            'pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'show_author': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'pinned': 'Закрепить объявление'
        }
