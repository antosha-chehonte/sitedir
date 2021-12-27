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
            # 'file',
            'style',
            'show_author',
            'is_published',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control', 'style': 'width:460px'}),
        }
