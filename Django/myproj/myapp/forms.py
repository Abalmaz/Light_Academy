from django import forms
from myapp.models import Task


class TaskForm(forms.Form):
    text = forms.CharField(max_length=20)
    checked = forms.BooleanField(required=False)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'checked']
        widgets = {'text': forms.Textarea()}

    def clean(self):
        text = self.cleaned_data['text']
        if text == 'lol':
            raise forms.ValidationError({'text': 'lol error'})
