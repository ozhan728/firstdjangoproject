from django import forms
from .models import Person

class TodoCreateForm(forms.Form) :
    name = forms.CharField(label='Nam',max_length=10)
    last_name = forms.CharField(max_length=20)
    number = forms.IntegerField()
    birthday = forms.DateTimeField(required=False)

class TodoUpdateForm(forms.ModelForm):
    class Meta :
        model = Person
        fields = ['name','last_name','number','birthday']

