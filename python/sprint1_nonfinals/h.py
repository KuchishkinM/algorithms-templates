from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first_number_list = []
    second_number_list = []
    for i in first_number:
        first_number_list.append(int(i))
    for i in second_number:
        second_number_list.append(int(i))
    first_number_list.reverse()
    second_number_list.reverse()
    size = max(len(first_number_list), len(second_number_list))
    first_number_list += [0] * (size - len(first_number_list))
    second_number_list += [0] * (size - len(second_number_list))
    remainder = 0
    result = []
    for i in zip(first_number_list, second_number_list):
        value = i[0] + i[1] + remainder
        remainder = value // 2
        result.append(value % 2)
    if remainder == 1:
        result.append(1)
    result = result[::-1]
    return ''.join(map(str, result))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
