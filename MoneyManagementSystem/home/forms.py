from django import forms
from .models import IncomeSource

class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ['source_name', 'amount', 'income_date', 'income_type']
