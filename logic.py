import numpy as np
import pandas as pd
import random

def creation_graphe(nb_sommit):
    return np.zeros((nb_sommit, nb_sommit), dtype=int)

def transformer_en_df(matrice):
    names = [f"S{i+1}" for i in range(len(matrice))]
    return pd.DataFrame(matrice, index=names, columns=names)

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
    
def creation_manuelle_matrice(matrice_df):
    nb_cols = matrice_df.shape[0]
    nb_index = matrice_df.shape[1]
    for i in range(nb_index):
        for j in range(i, nb_cols):
            if (i == j):
                matrice_df.iloc[i,j] = 0
            else:
                val = nombre_est_valide(matrice_df, i, j)
                matrice_df.iloc[i,j] = val
                matrice_df.iloc[j,i] = val
    print ( " MATRICE COMPLETE ")
    return matrice_df

def creation_automatic_matrice(matrice_df):
    nb_cols = matrice_df.shape[0]
    nb_index = matrice_df.shape[1]
    for i in range(nb_index):
        for j in range(i, nb_cols):
            if (i == j):
                matrice_df.iloc[i,j] = 0
            else:
                val = random.randint(0, 1)
                matrice_df.iloc[i,j] = val
                matrice_df.iloc[j,i] = val
    print ( " MATRICE COMPLETE ")
    return matrice_df