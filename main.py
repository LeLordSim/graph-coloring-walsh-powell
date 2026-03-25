from menus import main_menu, input_mode_menu
from logic import create_empty_matrix, transform_to_dataframe, create_manual_matrix, create_automatic_matrix
from viz import visualize_matrix

if __name__ == "__main__":
    node_count = main_menu()
    matrix_df = transform_to_dataframe(create_empty_matrix(node_count))
    
    mode = input_mode_menu()
    if mode == 1:
        final_df = create_manual_matrix(matrix_df)
    else:
        final_df = create_automatic_matrix(matrix_df)
        
    print(final_df)
    visualize_matrix(final_df)