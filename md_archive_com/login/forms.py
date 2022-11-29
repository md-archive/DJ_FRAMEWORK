from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="ToDo List Name", max_length=200)