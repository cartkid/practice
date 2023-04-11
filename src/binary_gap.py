def solution(N):
    # Implement your solution here
    binary = bin(N)
    # print(binary)
    found_b: bool = False
    curr_len: int = -1
    max_segment_len: int = -1
    in_valid_segment: bool = False
    for i in binary:
        if found_b is False or i == "b":
            found_b = True
            continue
        if i == "1":
            in_valid_segment = True
            if curr_len > 0 and curr_len > max_segment_len:
                max_segment_len = curr_len
            curr_len = 0
        if in_valid_segment and i == "0":
            curr_len += 1
    return 0 if max_segment_len == -1 else max_segment_len
