from django import forms
from .models import Task, Comments

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'expire_date', 'description', 'status', 'tag', 'priority']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']