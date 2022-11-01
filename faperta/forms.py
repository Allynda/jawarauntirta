from django.forms import ModelForm
from django import forms
from faperta.models import Dosen, Staf, Mahasiswa

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'Nip' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'TanggalLahir' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamat' : forms.TextInput({'class':'form-control'}),

        }

class FormStaf(ModelForm):
    class Meta:
        model = Staf
        fields = '__all__'

        widgets = {
            'Nip' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'TanggalLahir' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamat' : forms.TextInput({'class':'form-control'}),

        }

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'Nip' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'TanggalLahir' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamat' : forms.TextInput({'class':'form-control'}),

        }
