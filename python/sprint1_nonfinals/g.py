def to_binary(number: int) -> str:
    bi_number = []
    while number >= 1:
        bi_number.append(number % 2)
        number = number // 2
    bi_number_str = [str(i) for i in bi_number]
    bi_number_str.reverse()
    bi_number_str = ''.join(bi_number_str)
    return bi_number_str


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
