from django import forms
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'bio')

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
