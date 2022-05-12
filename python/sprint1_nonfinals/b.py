def check_parity(a: int, b: int, c: int) -> bool:
    mass = [abs(a), abs(b), abs(c)]
    nechet_counter = 0
    chet_counter = 0
    for i in mass:
        if i % 2 == 0:
            chet_counter += 1
        else:
            nechet_counter += 1
    if nechet_counter == 3 or chet_counter == 3:
        return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
