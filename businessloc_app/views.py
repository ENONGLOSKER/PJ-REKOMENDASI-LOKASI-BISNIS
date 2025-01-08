from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# multipel delete row
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# app
from . models import Alternatif, Kriteria, SubKriteria
from . forms import AlternatifForm, KriteriaForm,SubKriteriaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Berhasil')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username atau password salah.')

    return render(request, 'login.html')

def signout_user(request):
    logout(request)
    return redirect('index')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

# data alternatif
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