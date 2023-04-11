def sanitize(input: str) -> list[int]:
    # take in "a, b,   c, 1, 3, 4, 5, 6, 2"
    # return [1, 2, 3, 4, 5, 6]

    return_me: list[int] = []

    lst = input.split(",")
    return_me = list(set([int(x) for x in lst if x.strip().isnumeric()]))
    return_me.sort()
    return return_me
