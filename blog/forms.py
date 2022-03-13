from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comment form class
    """
    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)
