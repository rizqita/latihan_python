from django import forms
from .models import Mentee,Mentor,Blog

class inputMentee(forms.ModelForm):
    class Meta:
        model = Mentee
        fields=('nama','gambar','quote')
class inputMentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields=('nama','gambar','jabatan','durasi','quote')
class inputBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields=('judul','gambar','isi')