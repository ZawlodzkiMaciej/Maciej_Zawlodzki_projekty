# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:51:07 2019

@author: Maciej Zawłodzki
"""

class py_solution:
    def num_to_rom(self, a):
        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        rom_a = ''
        i = 0
        while  a > 0:
            for _ in range(a // value[i]):
                rom_a += symbol[i]
                a -= value[i]
            i += 1
        return rom_a

print(py_solution().num_to_rom(10))


class py_solution:
    def rom_to_num(self, b):
        rom_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in range(len(b)):
            if i > 0 and rom_value[b[i]] > rom_value[b[i - 1]]:
                int_value += rom_value[b[i]] - 2 * rom_value[b[i - 1]]
            else:
                int_value += rom_value[b[i]]
        return int_value

print(py_solution().rom_to_num('X'))