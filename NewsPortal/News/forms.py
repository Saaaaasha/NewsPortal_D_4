from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    category_type = forms.ChoiceField(
        label='Type',
        choices=Post.CATEGORY_TYPES
    )

    class Meta:
        model = Post
        fields = ['author', 'category_type',
                  'post_category',
                  'title', 'text']





