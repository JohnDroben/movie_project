from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Интерстеллар'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание сюжета фильма...',
                'rows': 4
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваши впечатления о фильме...',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
        labels = {
            'title': 'Название фильма',
            'description': 'Описание',
            'review': 'Ваш отзыв',
            'image': 'Постер фильма'
        }
