# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:26:55 2019

@author: Maciej Zawłodzki
"""
import math
class calculator():
    def dodawanie(self, a, b):
        wynik = a + b
        print(wynik)
    def odejmowanie(self, a, b):
        wynik = a - b
        print(wynik)
    def mnozenie(self, a, b):
        wynik = a * b
        print(wynik)
    def dzielenie(self, a, b):
        wynik = a / b
        print(wynik)
    def potegowanie(self, a, b):
        wynik = a ** b
        print(wynik)
    def pierwiastkowanie(self, a):
        wynik = math.sqrt(a)
        print(wynik)
    def logarytmnat(self, a):
        wynik = math.log(a)
        print(wynik)
    def exp(self, a):
        wynik = math.exp(a)
        print(wynik)
    def sinus(self, a):
        wynik = math.sin(a)
        print(wynik)
    def cosinus(self, a):
        wynik = math.cos(a)
        print(wynik)
    def stoprad(self, a):
        wynik = math.radians(a)
        print(wynik)
    def radstop(self, a):
        wynik = math.degrees(a)
        print(wynik)
    def silnia(self, a):
        wynik = math.factorial(a)
        print(wynik)
        
calc = calculator()
calc.dodawanie(5,5)
calc.odejmowanie(5,5)
calc.mnozenie(5,5)
calc.dzielenie(5,5)
calc.potegowanie(5,5)
calc.pierwiastkowanie(5)
calc.logarytmnat(5)
calc.exp(5)
calc.sinus(3.14/2)
calc.cosinus(0)
calc.stoprad(90)
calc.radstop(3.14/2)
calc.silnia(5)