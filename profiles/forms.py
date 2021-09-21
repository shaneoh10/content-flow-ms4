from django import forms
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'image')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
