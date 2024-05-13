from django import forms

class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ), widget=forms.RadioSelect())