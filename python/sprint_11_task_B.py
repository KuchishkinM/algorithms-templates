from typing import List, Tuple


def score_caliculate(k, matrix) -> int:
    only_digits = []
    values_of_digits = []
    for i in matrix:
        for j in i:
            if j != '.':
                only_digits.append(j)
                if j not in values_of_digits:
                    values_of_digits.append(j)
    counter = 0
    for i in values_of_digits:
        if only_digits.count(i) <= k * 2:
            counter += 1
    return counter


def read_input() -> Tuple[int, List[List[int]]]:
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append(list(input()))
    return k, matrix


k, matrix = read_input()
print(score_caliculate(k, matrix))
