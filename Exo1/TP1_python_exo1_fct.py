#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:11:42 2024
Script des fonctions qui permettent de donner la validité d'une date 
Amélioration :  ne vérifier qu'une fois dans tout le code que l'année est bien supérieur à 1582
@author: remi.cadusseau
"""

def Controle_annee_bissextile(pAn):
# fonction qui contrôle si une année est bissextile
# entrée ===> année (int 1582/2024)
# sortie ===> True/False   
    if pAn >= 1582 and pAn%4 == 0 and pAn%100 !=0:
        return True
    else:
        return False


def Controle_nbJour_dans_le_mois(pMo, pAn):
# fonction qui retourne le nombre de jour d'un mois
#entrée ===> mois (int 1/12) + année (int 1582/2024)
# sortie ===> int 31-30-29-28-0
    a = [1,3,5,7,8,10,12]
    b = 0
    if pMo <= 12 and pMo >= 1:
        if pMo == 2:
            if Controle_annee_bissextile(pAn) == True:
                return 29
            else:
                return 28
        for i in range(len(a)):
            if pMo == a[i]:
                b = 1
        if b == 1:
            return 31
        else:
            return 30
    else: 
        return 0
        
def Date_Valide(pJo,pMo,pAn):
# fonction qui vérifie si une date est valide
# entrée ===> jour/mois/année (int 1/31 1/12 1582/2024)
# sortie ===> True/false
    if pJo <= Controle_nbJour_dans_le_mois(pMo,pAn) and pJo >= 1 and pAn >= 1582:
        return True
    else:
        return False
    