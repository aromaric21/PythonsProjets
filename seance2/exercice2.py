# -*- coding: utf-8 -*-

def conversion(nombre):
    heures = nombre // 3600
    reste= nombre % 3600    
    minutes = reste // 60
    secondes = reste % 60
    print(nombre, "s =",heures, "heures", minutes, "minutes ", secondes, " secondes.")


def perimetre(longueur, largeur):
    return 2*(longueur + largeur)
    

conversion(11120)
#perimetre (39, 15)
print("Périmetre = ", perimetre (39, 15))


    
    