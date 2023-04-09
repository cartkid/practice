def balance_string(input: str) -> int:
    curr_letter = input[0] if input is not None and len(input) > 0 else "z"
    curr_count = 0
    max_count = None
    input_array = []
    for x in input:
        if x == curr_letter:
            curr_count += 1
        else:
            curr_letter = x
            input_array.append(curr_count)
            if max_count is None or max_count < curr_count:
                max_count = curr_count
            curr_count = 1
    input_array.append(curr_count)

    if max_count is None or max_count < curr_count:
        max_count = curr_count

    needed_letters = max_count * len(input_array)
    input_letters = len(input)

    return needed_letters - input_letters
