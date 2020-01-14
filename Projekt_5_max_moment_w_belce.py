# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:24:21 2020

@author: Maciej Zawłodzki
"""

class Belka:
    def rodzaj(self):
        pass
    def wypisz(self):
        print(f"Belka: {self.rodzaj()}, Dlugosc: {self.dlugosc()}, Sila: {self.sila()}, Max_Moment: {self.max_moment()}")
    def dlugosc(self):
        pass
    def sila(self):
        pass
    def max_moment(self):
        pass

class Wspornik(Belka):
    def __init__(self, L, P):
        self.L = L
        self.P = P
    def rodzaj(self):
        return "Wspornik"
    def dlugosc(self):
        return self.L
    def sila(self):
        return self.P
    def max_moment(self):
        return self.L * self.P

class Wolnopodparta(Belka):
    def __init__(self, L, P):
        self.L = L
        self.P = P
    def rodzaj(self):
        return "Wolnopodparta"
    def dlugosc(self):
        return self.L
    def sila(self):
        return self.P
    def max_moment(self):
        return (self.P * self.L)/4
    
def main():
    Ws = Wspornik(10.0, 3.0)
    Ws.wypisz()
    Wp = Wolnopodparta(10.0, 4.0)
    Wp.wypisz()

if __name__ == "__main__":
    main()