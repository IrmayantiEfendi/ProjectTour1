# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Destinasi, Reservasi
def index(request):
	destinasi = Destinasi.objects.all()
	context = {'destinasi':destinasi}
	return render(request,'aplikasi/index.html', context)

def destinasi(request):
	destinasi = Destinasi.objects.all()
	reservasi = Reservasi.objects.all()
	return render(request, 'aplikasi/pesantour.html',  {'reservasi':reservasi, 'destinasi':destinasi})

def pilih_reservasi(request, id):
	code_paket = Destinasi.objects.get(id=id)
	reservasi = Reservasi.objects.filter(code_paket=code_paket)
	context = {'reservasi':reservasi}
	return render(request, 'aplikasi/pesantour.html', context)

def reservasi(request):
	reservasi = Reservasi.objects.all()
	context = {'reservasi':reservasi}
	return render(request, 'aplikasi/pesantour.html', context)