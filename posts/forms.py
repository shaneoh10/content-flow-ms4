from django import forms
from .models import Post, Comment, Category


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'category': forms.Select(attrs={'class': 'form-control mb-3'}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'category': forms.Select(attrs={'class': 'form-control mb-3'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'image', 'description')

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
