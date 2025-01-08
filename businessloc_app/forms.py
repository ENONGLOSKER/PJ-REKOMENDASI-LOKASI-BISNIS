from django import forms
from .models import Alternatif, Kriteria, SubKriteria, Penilaian

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

class PenilaianForm(forms.ModelForm):
    class Meta:
        model = Penilaian
        fields = "__all__"

        widgets = {
            'alternatif': forms.Select(attrs={'class': 'form-control'}),
            'c1': forms.Select(attrs={'class': 'form-control'}),
            'c2': forms.Select(attrs={'class': 'form-control'}),
            'c3': forms.Select(attrs={'class': 'form-control'}),
            'c4': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PenilaianForm, self).__init__(*args, **kwargs)

        # Filter untuk kolom C1 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c1'].queryset = SubKriteria.objects.filter(kriteria__simbol='K1').order_by('nama')
        self.fields['c1'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C2 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c2'].queryset = SubKriteria.objects.filter(kriteria__simbol='K2').order_by('nama')
        self.fields['c2'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C3 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c3'].queryset = SubKriteria.objects.filter(kriteria__simbol='K3').order_by('nama')
        self.fields['c3'].label_from_instance = lambda obj: obj.nama

        # Filter untuk kolom C4 dan menampilkan nama namun saat disimpan akan mengambil nilainya
        self.fields['c4'].queryset = SubKriteria.objects.filter(kriteria__simbol='K4').order_by('nama')
        self.fields['c4'].label_from_instance = lambda obj: obj.nama