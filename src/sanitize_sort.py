def sanitize(input: str) -> list[int]:
    # take in "a, b,   c, 1, 3, 4, 5, 6, 2"
    # return [1, 2, 3, 4, 5, 6]

    return_me: list[int] = []

    lst = input.split(",")
    lst_of_numbers_as_string = list(filter(lambda item: item.strip().isnumeric(), lst))
    lst_of_numbers = list(map(lambda item: int(item), lst_of_numbers_as_string))
    return_me = list(set(lst_of_numbers))
    return_me.sort()

    return return_me
