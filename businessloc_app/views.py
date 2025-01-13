from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from decimal import Decimal
# multipel delete row
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# app
from . models import Alternatif, Kriteria, SubKriteria, Penilaian
from . forms import AlternatifForm, KriteriaForm,SubKriteriaForm, PenilaianForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard_alternatif')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Berhasil')
            return redirect('dashboard_alternatif')
        else:
            messages.error(request, 'Username atau password salah.')

    return render(request, 'login.html')

def signout_user(request):
    logout(request)
    return redirect('index')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

# DATA ALTERNATIF
def dashboard_alternatif(request):
    data_alternatif = Alternatif.objects.all()

    context = {
        'data_alternatif': data_alternatif,
    }
    return render(request, 'dashboard_alternatif.html', context)
def dashboard_alternatif_add(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_alternatif')
    else:
        form = AlternatifForm()

    data_alternatif = Alternatif.objects.all()
    

    context = {
        'data_alternatif': data_alternatif,
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
def dashboard_alternatif_update(request, id):
    alternatif = Alternatif.objects.get(id=id)
    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            return redirect('dashboard_alternatif')
    else:
        form = AlternatifForm(instance=alternatif)

    data_alternatif = Alternatif.objects.all()
    

    context = {
        'data_alternatif': data_alternatif,
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
def dashboard_alternatif_delete(request, id):
    alternatif = Alternatif.objects.get(id=id)
    alternatif.delete()
    return redirect('dashboard_alternatif')
# multipel delete row
@login_required()
@csrf_exempt
def dashboard_alternatif_delete_multiple(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ids = data.get("ids", [])

        if ids:
            Alternatif.objects.filter(id__in=ids).delete()
            return JsonResponse({"message": "Data berhasil dihapus."}, status=200)
        return JsonResponse({"error": "Tidak ada data yang dipilih."}, status=400)

    return JsonResponse({"error": "Metode tidak valid."}, status=405)

# DATA KRITERIA
@login_required()
def dashboard_kriteria(request):
    data_kriteria = Kriteria.objects.all()

    context = {
        'data_kriteria': data_kriteria,
    }
    return render(request, 'dashboard_kriteria.html', context)
@login_required()
def dashboard_kriteria_add(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_kriteria')
    else:
        form = KriteriaForm()

    data_kriteria = Kriteria.objects.all()

    context = {
        'data_kriteria': data_kriteria,
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
@login_required()
def dashboard_kriteria_update(request, id):
    kriteria = Kriteria.objects.get(id=id)
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('dashboard_kriteria')
    else:
        form = KriteriaForm(instance=kriteria)

    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
@login_required()
def dashboard_kriteria_delete(request, id):
    kriteria = Kriteria.objects.get(id=id)
    kriteria.delete()
    return redirect('dashboard_kriteria')
# multipel delete row
@login_required()
@csrf_exempt
def dashboard_kriteria_delete_multiple(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ids = data.get("ids", [])

        if ids:
            Kriteria.objects.filter(id__in=ids).delete()
            return JsonResponse({"message": "Data berhasil dihapus."}, status=200)
        return JsonResponse({"error": "Tidak ada data yang dipilih."}, status=400)

    return JsonResponse({"error": "Metode tidak valid."}, status=405)


# DATA SUBKRITERIA
def dashboard_subkriteria(request, id):
    data_kriteria = get_object_or_404(Kriteria, id=id)
    data_subkriteria = data_kriteria.subkriteria.all()

    context = {
        'data_kriteria': data_kriteria,
        'data_subkriteria': data_subkriteria,
    }
    return render(request, 'dashboard_sub_kriteria.html', context)
def dashboard_subkriteria_add(request):
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            sub_kriteria=form.instance
            return redirect('dashboard_subkriteria', id=sub_kriteria.kriteria.id)
    else:
        form = SubKriteriaForm()    
    context = {
        'form': form,
    }

    return render(request, 'dashboard_form.html', context)
def dashboard_subkriteria_update(request,id):
    data_kriteria = get_object_or_404(SubKriteria, id=id)
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST, instance=data_kriteria)
        if form.is_valid():
            form.save()
            sub_kriteria=form.instance
            return redirect('dashboard_subkriteria', id=sub_kriteria.kriteria.id)
    else:
        form = SubKriteriaForm(instance=data_kriteria)    
    context = {
        'form': form,
    }

    return render(request, 'dashboard_form.html', context)
def dashboard_subkriteria_delete(request,id):
    data_kriteria = get_object_or_404(SubKriteria, id=id)
    data_subkriteria = data_kriteria.kriteria.id
    data_kriteria.delete()
    return redirect('dashboard_subkriteria', id=data_subkriteria)

# DATA PENILAIAN
def dashboard_penilaian(request):
    data_penilaian = Penilaian.objects.all()
    kriteria_bobot = Kriteria.objects.values('nama', 'bobot', 'jenis')
    jlh_bobot = sum(kriteria['bobot'] for kriteria in kriteria_bobot)
    jlh_item_bobot = [{'index': idx, 'bobot': item['bobot'] / jlh_bobot, 'jenis': item['jenis']} for idx, item in enumerate(kriteria_bobot)]

    # Tahap 1: Mencari nilai pangkat sesuai dengan jenis kriteria
    hasil_pangkat = {
        item['index']: item['bobot'] * (1 if item['jenis'] == 'BENEFIT' else -1)
        for item in jlh_item_bobot
    }

    tabel_penilaian = [
        {
            'no': idx + 1,
            'alternatif': p.alternatif,
            'c1': p.c1.nilai ** Decimal(hasil_pangkat[0]),  
            'c2': p.c2.nilai ** Decimal(hasil_pangkat[1]),  
            'c3': p.c3.nilai ** Decimal(hasil_pangkat[2]),  
            'c4': p.c4.nilai ** Decimal(hasil_pangkat[3]), 
            'hasil': (
                (p.c1.nilai ** Decimal(hasil_pangkat[0])) *
                (p.c2.nilai ** Decimal(hasil_pangkat[1])) *
                (p.c3.nilai ** Decimal(hasil_pangkat[2])) *
                (p.c4.nilai ** Decimal(hasil_pangkat[3]))
            )
        }
        for idx, p in enumerate(data_penilaian)
    ]

    # Tahap 2: Mengelompokkan dan menjumlahkan hasil per alternatif
    total_per_alternatif = defaultdict(Decimal)
    for item in tabel_penilaian:
        total_per_alternatif[item['alternatif']] += item['hasil']

    # Tahap 3: menentukan vektor v yaitu hasil dari tabel penilain dibagi dengan total dari data tabel penilain
    penilaian_data = []
    total_semua_alternatif = sum(total_per_alternatif.values())  # Jumlahkan semua hasil total per alternatif
    for idx, item in enumerate(tabel_penilaian):
        hasil_per_alternatif = item['hasil'] / total_semua_alternatif  # Bagi setiap alternatif dengan hasil penjumlahan atau total tersebut
        # print('-----------------------------------')
        # print('hasil per alternatif :', hasil_per_alternatif)
        # print('item :', item['hasil'])
        # print('total semua alternatif :', total_semua_alternatif)
        
        penilaian_data.append({
            'no': idx + 1,
            'alternatif': item['alternatif'],
            'hasil': hasil_per_alternatif,
            'rekomendasi': None,  # Placeholder untuk rekomendasi
        })
    # print('penilaian_data :', penilaian_data)

    # urutkan penilaian_data berdasrkan yang terbesar ke yang terkecil dan tambahkan kolom rekomendasi
    penilaian_data.sort(key=lambda x: x['hasil'], reverse=True)

    for idx, item in enumerate(penilaian_data):
        if idx == 0:
            item['rekomendasi'] = 'Direkomendasikan'
        else:
            item['rekomendasi'] = 'Tidak Direkomendasikan'

    context = {
        'data_penilaian':data_penilaian,
        'bobot': kriteria_bobot,
        'jlh_bobot': jlh_bobot,
        'jlh_item_bobot': jlh_item_bobot,
        'hasil_pangkat': hasil_pangkat,
        'tabel_penilaian': tabel_penilaian,
        'penilaian_data': penilaian_data,
    }
    return render(request, 'dashboard_penilaian.html', context)

@login_required
def dashboard_penilaian_add(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_penilaian')
    else:
        form = PenilaianForm()
    return render(request, 'dashboard_form.html', {'form': form})
def dashboard_penilaian_update(request,id):
    penilaian = get_object_or_404(Penilaian, id=id)
    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('dashboard_penilaian')
    else:
        form = PenilaianForm(instance=penilaian)
    return render(request, 'dashboard_form.html', {'form': form})

def dashboard_penilaian_delete(request,id):
    penilaian = get_object_or_404(Penilaian, id=id)
    penilaian.delete()
    return redirect('dashboard_penilaian')