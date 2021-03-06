from django import forms
from .models import *


class AddSort(forms.ModelForm):
    class Meta:
        model = SortingForm
        fields = ['algorithm', 'input_file']
