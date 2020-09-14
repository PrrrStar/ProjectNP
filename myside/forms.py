from . import forms

from .models import Comment
from .models import Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'created_at']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'created_at']