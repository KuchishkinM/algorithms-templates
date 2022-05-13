from typing import List


def factorize(number: int) -> List[int]:
    integers = []
    s = 2
    while s * s <= number:
        if number % s == 0:
            integers.append(s)
            number //= s
        else:
            s += 1
    integers.append(number)
    return integers


result = factorize(int(input()))
print(" ".join(map(str, result)))
