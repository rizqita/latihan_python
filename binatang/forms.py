from django import forms
from .models import Hewan

class inputHewan(forms.ModelForm):

    class Meta:
        model = Hewan
        fields= ('nama','species','berat','umur')