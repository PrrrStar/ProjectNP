from .models import Comment
from .models import Reply

from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','img','stars')
        widgets={
            "content":forms.TextInput(attrs={
                'class': 'mycomment__content',
                'name': 'content',
                'placeholder': '댓글 입력'
            }),
            "img":forms.FileInput(attrs={
                'class': 'mycomment__img',
                'name': 'img',
            }),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content',]