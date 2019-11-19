# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:45:58 2019

@author: Maciej Zawłodzki
"""

import numpy as np

OkresSplaty = float(input("Okres spłaty wynosi (liczba miesięcy): "))
KwotaNetto = float(input("Kwota netto wynosi (zł): "))
Oprocentowanie = float(input("Oprocentowanie (%): "))
Prowizja = float(input("Prowizja (%): "))

KwotaBrutto = round(KwotaNetto / (1 - (Prowizja/100)), 2)

RataKredytu = round(np.pmt((Oprocentowanie/100)/12, OkresSplaty, KwotaBrutto), 2)

DodatniaRataKredytu = abs(RataKredytu)
LacznaKwotaDoSplacenia = abs(round(RataKredytu*OkresSplaty, 2))

print(30*"-")
print(f"Kwota netto: {KwotaNetto} zł")
print(f"Kwota brutto: {KwotaBrutto} zł")
print(f"Oprocentowanie: {Oprocentowanie} %")
print(f"Prowizja: {Prowizja} %")
print(f"Rata kredytu: {DodatniaRataKredytu} zł")
print(f"Łączna kwota do spłaty: {LacznaKwotaDoSplacenia} zł")
print(30*"-")