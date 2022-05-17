from typing import List, Tuple


def length_caliculate(street_length: int, number_list: List[int]) -> List[int]:
    zero_index = 0
    left_zero = number_list.index(0)
    for i in range(left_zero, street_length):
        if number_list[i] == 0:
            number_list[i] = 0
            zero_index = i
        number_list[i] = i - zero_index
    for i in range(zero_index, left_zero, -1):
        if number_list[i] == 0:
            number_list[i] = 0
            zero_index = i
        number_list[i] = min(abs(i - zero_index), number_list[i])
    for i in range(left_zero, -1, -1):
        number_list[i] = abs(left_zero - i)
    return number_list


def read_input() -> Tuple[int, List[int]]:
    street_length = int(input())
    number_list = list(map(int, input().strip().split()))
    return street_length, number_list


street_length, number_list = read_input()
print(*(length_caliculate(street_length, number_list)))
