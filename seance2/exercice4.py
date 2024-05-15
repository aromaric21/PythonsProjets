# -*- coding: utf-8 -*-

nom = "Adjei"
prenom = "Romaric"

# Le code est formé par les deux premières lettres ddu nom et la dernière lettre du prénom
code = nom[:2] + prenom[-1]

# Affichage du code en majuscule
print(code.upper())


# Les moitiés respectives du nom et du prénom
moitieNom = len(nom) // 2
print(moitieNom)

moitiePrenom = len(prenom) // 2
print(moitiePrenom)

# Obtenir les deux deuxièmes moitiés, respectivement, du nom et du prénom
extrait1 = nom[moitieNom : ]
print(extrait1)

extrait2 = prenom[moitiePrenom : ]
print(extrait2)

# Je les renverses
inverse_extrait1 = extrait1[: :-1]
print(inverse_extrait1)

inverse_extrait2 = extrait2[: :-1]
print(inverse_extrait2)

# Concatenation puis affichage répété 3 fois
motDePasse = inverse_extrait1 + inverse_extrait2
print(motDePasse*3)
