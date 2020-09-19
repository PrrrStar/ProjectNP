from .models import Comment
from .models import Reply

from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','author','img',]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content',]