def is_palindrome(input: str) -> bool:
    test = input[::-1]
    return test == input


def is_palindrome2(input: str) -> bool:
    up_to_index: int = int(len(input) / 2)
    if len(input) % 2 == 0:
        up_to_index -= 1
    print(f"{len(input)}: {up_to_index}")
    test = input[:up_to_index:-1]
    print(f"{input}: {test}")
    return input.startswith(test)


def is_palindrome3(input: str) -> bool:
    up_to_index: int = int(len(input) / 2)
    print(f"{len(input)}: {up_to_index}")
    for i in range(up_to_index):
        if input[i] == input[len(input) - 1 - i]:
            continue
        else:
            return False
    return True
