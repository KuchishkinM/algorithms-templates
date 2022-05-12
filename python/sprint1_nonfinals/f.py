import re


def is_palindrome(line: str) -> bool:
    new_text = re.sub(r'[^A-z0-9]', '', line).lower()

    revers_text = new_text[::-1]

    if new_text == revers_text:
        return True
    else:
        return False


print(is_palindrome(input().strip()))
