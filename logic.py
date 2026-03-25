import numpy as np
import pandas as pd
import random
from menus import validate_edge_input

def create_empty_matrix(node_count):
    return np.zeros((node_count, node_count), dtype=int)

def transform_to_dataframe(matrix):
    size = len(matrix)
    names = [f"S{i+1}" for i in range(size)]
    return pd.DataFrame(matrix, index=names, columns=names)

def create_manual_matrix(matrix_df):
    size = matrix_df.shape[0]
    for i in range(size):
        for j in range(i, size):
            if i == j:
                matrix_df.iloc[i, j] = 0
            else:
                val = validate_edge_input(matrix_df, i, j)
                matrix_df.iloc[i, j] = val
                matrix_df.iloc[j, i] = val
    print("MATRIX COMPLETED")
    return matrix_df

def create_automatic_matrix(matrix_df):
    size = matrix_df.shape[0]
    for i in range(size):
        for j in range(i, size):
            if i == j:
                matrix_df.iloc[i, j] = 0
            else:
                val = random.randint(0, 1)
                matrix_df.iloc[i, j] = val
                matrix_df.iloc[j, i] = val
    print("MATRIX COMPLETED")
    return matrix_df