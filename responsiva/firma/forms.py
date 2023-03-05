from django import forms
from jsignature.forms import JSignatureField
import json
from django.forms.fields import Field
from django.core import validators
from django.core.exceptions import ValidationError
from .widgets import JSignatureWidget


class SignatureForm(forms.Form):
    signature = JSignatureField()

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

JSIGNATURE_EMPTY_VALUES = validators.EMPTY_VALUES + ('[]', )


class JSignatureField(Field):
    """
    A field handling a signature capture field with with jSignature
    """
    widget = JSignatureWidget()

    def to_python(self, value):
            """
            Validates that the input can be red as a JSON object.
            Returns a Python list (JSON object unserialized).
            """
            if value in JSIGNATURE_EMPTY_VALUES:
                return None
            try:
                return json.loads(value)
            except ValueError:
                raise ValidationError('Invalid JSON format.')
            
# forms.py
from django import forms
from jsignature.forms import JSignatureField

class SignatureForm(forms.Form):
    signature = JSignatureField()