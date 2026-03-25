from menus import menu_choice_1, menu_choice_2
from logic import creation_graphe, transformer_en_df, creation_manuelle_matrice, creation_automatic_matrice
from viz import visualiser_matrice
if __name__ == "__main__":
    nb = menu_choice_1()
    df = transformer_en_df(creation_graphe(nb))
    mode = menu_choice_2()
    if mode == 1:
        df_final = creation_manuelle_matrice(df)
    else:
        df_final = creation_automatic_matrice(df)
        
    print(df_final)
    visualiser_matrice(df_final)