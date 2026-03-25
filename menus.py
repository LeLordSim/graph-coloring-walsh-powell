import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def menu_choice_1():
    while True:
        try:
            choice = int(input("Tapez 1 pour créer un graphe || Tapez 2 pour faire l'algorithme : "))
            if choice == 1:
                try:
                    
                    nb_sommit = int(input("Nombre de sommets de la matrice a créer (maximum 10): "))
                    if 1 <= nb_sommit <= 10:
                        return nb_sommit
                    else:
                        print("ERREUR : le nombre choisi doit être compris entre 1 et 10 inclus.")
                except ValueError:
                    ("ERREUR : Veuillez entrer un nombre entier valide.")
            else:
                print("ERREUR : le nombre choisi doit être 1 ou 2.")
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre entier valide.")




def menu_choice_2():
    while True:
        try:
            choice = int(input("Tapez 1 pour créer manuellement le graphe || Tapez 2 pour générer un graphe valide : "))
            if choice not in [1,2]:
                print("ERREUR : le nombre choisi doit être 1 ou 2.")
            else:
                return choice
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre entier valide.")
         
def nombre_est_valide(matrice_df, index, colums):
    while True:
        try:
            print(matrice_df)
            choice = int(input(f"Tapez 0 ou 1 pour le nombre en [S{index+1}, S{colums+1}] : "))
            if choice not in [0,1]:
                print("ERREUR : le nombre choisi doit être 0 ou 1.")
            else:
                return choice
        except ValueError:
            print("ERREUR : Veuillez entrer un nombre entier valide.")






