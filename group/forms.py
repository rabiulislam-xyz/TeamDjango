from django import forms


class MessageCreateForm(forms.Form):
    content = forms.CharField()
