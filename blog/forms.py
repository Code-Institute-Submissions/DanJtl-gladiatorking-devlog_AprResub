from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comment form class
    """
    body = forms.CharField(required=True, max_length=250)

    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)
