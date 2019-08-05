from django import forms

class InputForm(forms.Form):
    input = forms.CharField(label='Matrix1' , max_length=100, widget=forms.Textarea())
