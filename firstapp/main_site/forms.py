from .models import Table
from django.forms import ModelForm, TextInput, Textarea


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['title', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'}),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the description'}),
            }
