from django import forms
from . models import Review

class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs = {
                'class': 'form-control',
                'maxlength': 70,
            }
        )
    )
    score = forms.FloatField(
        label='It would be 10 out of ...',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'min':1, 'step':1, 'max':10, 'type':'number'
                }
            ),
        )

    class Meta:
        model = Review
        fields = ('content', 'score', )