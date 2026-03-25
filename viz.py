import numpy as np
import matplotlib.pyplot as plt

def visualiser_matrice(matrice_df_comp):
    name_graphe = input("Nom de votre graphe: ")
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.axis('off')
    ax.set_aspect('equal')
    angles = np.linspace(0, np.pi*2, len(matrice_df_comp.columns), endpoint = False)
    pos_x = np.cos(angles)
    pos_y = np.sin(angles)
    ax.scatter(pos_x, pos_y, s=1500, c='skyblue', edgecolors='black', zorder=2)
    n = len(matrice_df_comp.columns)
    for i in range(n):
        for j in range(i + 1, n):
            if matrice_df_comp.iloc[i, j] == 1:
                ax.plot([pos_x[i], pos_x[j]], [pos_y[i], pos_y[j]], color='gray', zorder=1)
    for i, nom in enumerate(matrice_df_comp.columns):
        ax.text(pos_x[i], pos_y[i], nom, ha='center', va='center', fontweight='bold', zorder=3)
    plt.title(name_graphe, fontsize=16, pad=50)
    plt.show()