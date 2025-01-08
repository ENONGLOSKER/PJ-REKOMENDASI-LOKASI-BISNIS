from django.db import models

# Create your models here.
class Alternatif(models.Model):
    simbol = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nama
    
class Kriteria(models.Model):
    JS = [('BENEFIT', 'BENEFIT'),('COST','COST')]

    simbol = models.CharField(max_length=5)
    nama = models.CharField(max_length=50)
    bobot = models.FloatField(default=0)  # Nilai bobot antara 0-1
    jenis = models.CharField(choices=JS, default='benefit', max_length=10)

    def __str__(self) -> str:
        return self.nama
    
class SubKriteria(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE, related_name='subkriteria')
    nama = models.CharField(max_length=100)
    nilai = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.nilai}"

class Penilaian(models.Model):
    alternatif = models.ForeignKey(Alternatif, on_delete=models.CASCADE, related_name='penilaian_al')
    c1 = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_c1', limit_choices_to={'kriteria__simbol': 'K1'})
    c2 = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_c2', limit_choices_to={'kriteria__simbol': 'K2'})
    c3 = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_c3', limit_choices_to={'kriteria__simbol': 'K3'})
    c4 = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_c4', limit_choices_to={'kriteria__simbol': 'K4'})

    def __str__(self):
        return f"{self.alternatif.nama} - {self.ekskul.nama} (C1: {self.c1.nilai}, C2: {self.c2.nilai}, C3: {self.c3.nilai}, C4: {self.c4.nilai})"
    