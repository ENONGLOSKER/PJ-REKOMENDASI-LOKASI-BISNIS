from django import forms
from .models import Alternatif, Kriteria, SubKriteria

class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = '__all__'
        widgets = {
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
        }

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = "__all__"
        widgets = {
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'bobot': forms.NumberInput(attrs={'class': 'form-control'}),
            'jenis': forms.Select(attrs={'class': 'form-control'}),
        }

class SubKriteriaForm(forms.ModelForm):
    class Meta:
        model = SubKriteria
        fields = '__all__'
        widgets = {
            'kriteria': forms.Select(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai': forms.NumberInput(attrs={'class': 'form-control'}),
        }
