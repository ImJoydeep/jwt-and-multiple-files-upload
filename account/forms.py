from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from .models import Document

class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
