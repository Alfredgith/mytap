from django import forms
from .models import cas


class mycas(forms.ModelForm):
      class Meta:
            model=cas
            fields='__all__'