def hailstone(n: int) -> int:
    print(f"{n}: ")
    count = 0
    if n == 0:
        return count
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        print(f"\t{n}")
    return count
