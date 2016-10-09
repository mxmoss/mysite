from django import forms

from .models import myRecord

class PostForm(forms.ModelForm):

    class Meta:
        model = myRecord
