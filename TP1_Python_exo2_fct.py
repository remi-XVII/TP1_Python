#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:52:32 2024
Script de la fonctions qui permets pour un revenu de donné le montant des impots à payer
@author: remi.cadusseau
"""

def mesImpots (pR,pT,pI):
    """
    fonction qui calcul le montant d'impot à payer pour un revenu donné
    entrée ===> int, liste de listes [[int]], liste [int]
    sortie ===> int
    """
    for i in range(len(pT)):
        if pR >= pT[i][0] and pR <= pT[i][1]:
            a = (pR-pT[i][0]) * (pI[i]/100)
            b = int(a)
            return b
        
        