def isHappy(n: int) -> bool:
    n_str: str = str(n)
    curr_sum: int = 0
    for digit in n_str:
        curr_int_digit = int(digit)
        curr_sum += curr_int_digit * curr_int_digit
    if curr_sum == 1:
        return True
    if len(n_str) == 1:
        return False
    return isHappy(curr_sum)
