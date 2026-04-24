def matrix_sum(
    matrix_1: list[list[int]], matrix_2: list[list[int]]
) -> list[list[int]] | None:
    # Write a function that takes two matrices and calculates the sum.
    # Ensure that the matrices are compatible before summing. Inform the user if not.
    # Return the output matrix
    
    # 1. Check shapes of matrices to ensure compatibility
    is_row_compatible = len(matrix_1) == len(matrix_2)
    is_col_compatible = len(matrix_1[0]) == len(matrix_2[0])

    if is_row_compatible and is_col_compatible:
        print("All good, calculating sum...")
    else:
        print("Shapes mismatched, aborting")
        return None

    # 2. Initialize output matrix
    n_rows = len(matrix_1)
    n_cols = len(matrix_1[0])
    result_matrix = [None for i in n_rows for j in n_cols]

    # 3. Store sum
    for i in range(n_rows):
        for j in range(n_cols):
            result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

    # 4. Return results
    return result_matrix


def matrix_prod(
    matrix_1: list[list[int]], matrix_2: list[list[int]]
) -> list[list[int]] | None:
    # Implement this function
    raise NotImplementedError


if __name__ == "__main__":
    mat1 = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]
    mat2 = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]

    mat_sum_res = matrix_sum(mat1, mat2)
    mat_prod_res = matrix_prod(mat1, mat2)
    print(mat_sum_res)
    print(mat_prod_res)