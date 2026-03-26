import numpy as np
import matplotlib.pyplot as plt

def visualize_matrix(matrix_df):
    graph_name = input("Enter graph title: ")
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.axis('off')
    ax.set_aspect('equal')
    
    node_count = len(matrix_df.columns)
    angles = np.linspace(0, np.pi*2, node_count, endpoint=False)
    pos_x = np.cos(angles)
    pos_y = np.sin(angles)
    
    for i in range(node_count):
        for j in range(i + 1, node_count):
            if matrix_df.iloc[i, j] == 1:
                ax.plot([pos_x[i], pos_x[j]], [pos_y[i], pos_y[j]], color='gray', zorder=1)
                
    ax.scatter(pos_x, pos_y, s=1500, c='skyblue', edgecolors='black', zorder=2)
    
    for i, name in enumerate(matrix_df.columns):
        ax.text(pos_x[i], pos_y[i], name, ha='center', va='center', fontweight='bold', zorder=3)
    
    plt.title(graph_name, fontsize=16, pad=40)
    plt.margins(0.2)
    plt.show()