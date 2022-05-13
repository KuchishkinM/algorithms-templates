from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    mass = []
    for i in number_list:
        mass.append(str(i))
    s = ''.join(mass)
    result = int(s) + k
    result_list = []
    for i in str(result):
        result_list.append(int(i))
    return result_list


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
