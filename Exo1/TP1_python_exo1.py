#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:11:37 2024
Scrit qui permet de donner la validité d'une date à rentrer sur la console
Amélioration : plus de contrôle dans la sélection de la date par l'utilisateur dans la commande
@author: remi.cadusseau
"""

from TP1_python_exo1_fct import Controle_annee_bissextile , Controle_nbJour_dans_le_mois , Date_Valide

a = 2024
b = 2025
c = 1582
d = 1581
e = 2016
f = 2011
g = 2000

h = 1
i = 2
j = 12
k = 13

l = 31
m = 32
n = 29

jour = int(input("saisir le jour: "))
mois = int(input("saisir le mois: "))
annee = int(input("saisir l'année: "))

date = Date_Valide(jour,mois,annee)
if date == True:
    print("la date est valide")
else:
    print("la date n'est pas valide")