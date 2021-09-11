import re
from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator

from .models import ImageModel


class ImageForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']


class ColorForm(forms.Form):
    re_hex = re.compile('^#[0-9a-fA-F]{6}$')
    hex_validator = RegexValidator(
        re_hex,
        'Введите корректный hex код. Например #aabbcc'
    )
    hex_color = forms.CharField(
        label="HEX код",
        max_length=7,
        min_length=7,
        help_text="Введите hex код",
        validators=[hex_validator]
    )
