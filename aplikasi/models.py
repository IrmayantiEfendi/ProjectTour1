# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Destinasi(models.Model):
	Tempat = models.CharField(max_length=40)

class Reservasi(models.Model):
	Destinasi = models.CharField(max_length=40)
	Paket = models.CharField(max_length=40)
	Min_pax = models.IntegerField()
	Biaya = models.FloatField()
	code_paket = models.IntegerField()