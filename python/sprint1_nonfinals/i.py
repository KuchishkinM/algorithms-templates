def is_power_of_four(number: int) -> bool:
    EXPONENT = 4
    if EXPONENT == number or number == 1:
        return True
    while EXPONENT <= number:
        EXPONENT *= 4
        if EXPONENT == number:
            return True
    else:
        return False


print(is_power_of_four(int(input())))
