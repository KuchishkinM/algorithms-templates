from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    if row != max_row:
        result.append(matrix[row + 1][col])
    if row != 0:
        result.append(matrix[row - 1][col])
    if col != max_col:
        result.append(matrix[row][col + 1])
    if col != 0:
        result.append(matrix[row][col - 1])
    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
