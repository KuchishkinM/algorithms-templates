def get_longest_word(line: str) -> str:
    line = line.split(' ')
    word = ''
    for i in line:
        if len(i) > len(word):
            word = i
    return word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
