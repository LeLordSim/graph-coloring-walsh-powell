def main_menu():
    while True:
        try:
            choice = int(input("Press 1 to create a graph || Press 2 for the algorithm : "))
            if choice == 1:
                try:
                    node_count = int(input("Number of nodes (max 10): "))
                    if 1 <= node_count <= 10:
                        return node_count
                    else:
                        print("ERROR: Number must be between 1 and 10.")
                except ValueError:
                    print("ERROR: Please enter a valid integer.")
            else:
                print("ERROR: Choice must be 1 or 2.")
        except ValueError:
            print("ERROR: Please enter a valid integer.")

def input_mode_menu():
    while True:
        try:
            choice = int(input("Press 1 for Manual creation || Press 2 for Automatic generation: "))
            if choice in [1, 2]:
                return choice
            print("ERROR: Choice must be 1 or 2.")
        except ValueError:
            print("ERROR: Please enter a valid integer.")

def validate_edge_input(matrix_df, row_idx, col_idx):
    while True:
        try:
            print(matrix_df)
            choice = int(input(f"Enter 0 or 1 for edge [S{row_idx+1}, S{col_idx+1}]: "))
            if choice in [0, 1]:
                return choice
            print("ERROR: Value must be 0 or 1.")
        except ValueError:
            print("ERROR: Please enter a valid integer.")