from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    two_words = sorted(shorter + longer)
    letters = []
    for i in two_words:
        letters.append(two_words.count(i))
    extra_letter = []
    for i in range(len(letters)):
        if letters[i] % 2 != 0:
            extra_letter.append(two_words[i])
            break
    return str(*extra_letter)


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
