from django import forms
from persons.models import Persons
class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = "__all__" 
