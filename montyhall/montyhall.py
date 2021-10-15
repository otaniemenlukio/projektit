#! /usr/bin/env python3

import random

n = int(input('Syötä kierroksien määrä: '))

voitot_ei_vaihtoa = 0
voitot_vaihto = 0
for i in range(n):
    ovet = [True, False, False]
    random.shuffle(ovet)
    arvaus = random.randint(0,2)
    ovet.pop(arvaus)
    ovet.remove(False)
    if ovet[0]:
        voitot_vaihto += 1
    else:
        voitot_ei_vaihtoa += 1

print(f'Voitot ilman vaihtoa: {voitot_ei_vaihtoa}')
print(f'Voitot vaihdolla: {voitot_vaihto}')
