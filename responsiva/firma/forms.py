from django import forms
from jsignature.forms import JSignatureField

class SignatureForm(forms.Form):
    signature = JSignatureField()

from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))