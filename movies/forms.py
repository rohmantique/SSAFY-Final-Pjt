from django import forms
from . models import Review

class ReviewForm(forms.ModelForm):
    content = forms.TextInput(
        attrs = {
            'class': 'form-control',
        }
    )
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'min':0, 'step':1, 'max':10, 'type':'number'
                }
            ),
        )

    class Meta:
        model = Review
        fields = ('content', 'score', )