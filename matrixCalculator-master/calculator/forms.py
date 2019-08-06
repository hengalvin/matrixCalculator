from django import forms

class InputForm(forms.Form):
    input = forms.CharField(label='Matrix' , max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Input square matrix', 'cols': "46"}))
