import numpy as np

def find_s_special_elements(matrix):
    rows, cols = matrix.shape
    special_elements = []

    for i in range(rows):
        row_sum = np.sum(matrix[i, :])
        for j in range(cols):
            if matrix[i, j] > row_sum - matrix[i, j]:
                special_elements.append((matrix[i, j], i, j))

    return special_elements

def find_max_s_special_element(matrix):
    special_elements = find_s_special_elements(matrix)
    if not special_elements:
        return None, None, None, None

    max_element, max_row, max_col = max(special_elements, key=lambda x: (x[0], -x[1]))
    return max_element, max_row, max_col, max_row + 1

# Приклад використання
matrix = np.array([
    [50, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 50],
    [13, 14, 15, 16]
])

max_element, max_row, max_col, row_number = find_max_s_special_element(matrix)

if max_element is not None:
    print(f"Максимальний S-особливий елемент: {max_element}")
    print(f"Номер рядка: {row_number}")
    print(f"Індекси елемента: ({max_row+1}, {max_col+1})")
else:
    print("таких нема!")
