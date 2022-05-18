# ID 68467358
from collections import Counter
from typing import List, Tuple


def score_caliculate(k, matrix) -> int:
    only_digits = []
    for i in matrix:
        for j in i:
            if j != '.':
                only_digits.append(j)
    counter = 0
    for i in Counter(only_digits).values():
        if i <= k * 2:
            counter += 1
    return counter


def read_input() -> Tuple[int, List[List[int]]]:
    k = int(input())
    matrix = []
    for i in range(4):
        matrix.append(list(input()))
    return k, matrix


def main():
    k, matrix = read_input()
    print(score_caliculate(k, matrix))


if __name__ == '__main__':
    main()
