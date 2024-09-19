#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:52:31 2024
Script qui permet de connaitre le montant d'impôt à payer pour un revenu renseigné dans la console par l'utilisateur
@author: remi.cadusseau
"""

from TP1_Python_exo2_fct import mesImpots

tranche = [[0,10225],[10226,26070],[26071,74545],[74546,160336],[160336,10000000000000000000000000000000]]
taux = [0,11,30,41,45]

revenu = int(input("saisir vos revenus: "))
impot = mesImpots(revenu,tranche,taux)
print("vous devez payer",impot)
