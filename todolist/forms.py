from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=50)
    widget = forms.TextInput(
        attrs={'type':'text', 'id':'todoItem', 'placeholder':'Enter todo. e.g Get more food stuff'}
    )