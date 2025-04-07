from django import forms
from .models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'gender', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
