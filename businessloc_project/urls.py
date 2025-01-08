"""
URL configuration for businessloc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from businessloc_app import views
# static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signin/', views.signin_user, name='signin'),
    path('signout/', views.signout_user, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # kriteria
    path('dashboard/kriteria/', views.dashboard_kriteria, name='dashboard_kriteria'),
    path('dashboard/kriteria/add/', views.dashboard_kriteria_add, name='dashboard_kriteria_add'),
    path('dashboard/kriteria/update/<int:id>/', views.dashboard_kriteria_update, name='dashboard_kriteria_update'),
    path('dashboard/kriteria/delete/<int:id>/', views.dashboard_kriteria_delete, name='dashboard_kriteria_delete'),
    path('dashboard/kriteria/delete-multiple/', views.dashboard_kriteria_delete_multiple, name='dashboard_kriteria_delete_multiple'),
    # subkriteria
    path('dashboard/subkriteria/<int:id>/', views.dashboard_subkriteria, name='dashboard_subkriteria'),
    path('dashboard/subkriteria/add/', views.dashboard_subkriteria_add, name='dashboard_subkriteria_add'),
    path('dashboard/subkriteria/update/<int:id>/', views.dashboard_subkriteria_update, name='dashboard_subkriteria_update'),
    path('dashboard/subkriteria/delete/<int:id>/', views.dashboard_subkriteria_delete, name='dashboard_subkriteria_delete'),
    # alternatif
    path('dashboard/alternatif/', views.dashboard_alternatif, name='dashboard_alternatif'),
    path('dashboard/alternatif/add/', views.dashboard_alternatif_add, name='dashboard_alternatif_add'),
    path('dashboard/alternatif/update/<int:id>/', views.dashboard_alternatif_update, name='dashboard_alternatif_update'),
    path('dashboard/alternatif/delete/<int:id>/', views.dashboard_alternatif_delete, name='dashboard_alternatif_delete'),
    path('dashboard/alternatif/delete-multiple/', views.dashboard_alternatif_delete_multiple, name='dashboard_alternatif_delete_multiple'),
    # penilaian
    path('dashboard/penilaian/', views.dashboard_penilaian, name='dashboard_penilaian'),
    path('dashboard/penilaian/add/', views.dashboard_penilaian_add, name='dashboard_penilaian_add'),
    path('dashboard/penilaian/update/<int:id>/', views.dashboard_penilaian_update, name='dashboard_penilaian_update'),
    path('dashboard/penilaian/delete/<int:id>/', views.dashboard_penilaian_delete, name='dashboard_penilaian_delete'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


