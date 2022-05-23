from django import forms
from . models import Mood, Review

class MoodForm(forms.ModelForm):
    status = forms.ChoiceField(
        label='status',
        widget=forms.Select(
            attrs={
                'class': 'form-select form-control',
            }
        ),
        choices=[
            ('설렘', '설렘'),
            ('우울', '우울'),
            ('활기찬', '활기찬'),
            ('에너지가 필요한', '에너지가 필요한'),
            ('진정이 필요한', '진정이 필요한')
            ]
    )

    class Meta:
        model = Mood
        fields = ('status', )

class ReviewForm(forms.Form):
    content = forms.TextInput(
        attrs = {
            'class': 'form-control',
        }
    )
    score = forms.FloatField()

    class Mega:
        model = Review
        fields = ('content', 'score', )