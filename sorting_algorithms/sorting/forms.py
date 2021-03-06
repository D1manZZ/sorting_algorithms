from django import forms
from .models import *


class AddSort(forms.ModelForm):

    model = SortingData
    fields = ['algorithm', 'input_file']
    widgets = {
        'algorithm': forms.TextInput(attrs={'class': 'form-control'})
    }
