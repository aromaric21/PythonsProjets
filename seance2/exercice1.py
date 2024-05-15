# -*- coding: utf-8 -*-


def nbChiffres(nombre, chiffre):
    return str(nombre).count(str(chiffre))


occurence = nbChiffres(222324258924, 2)
print(occurence)