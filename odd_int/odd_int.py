def odd_int(seq):
    result = 0
    for num in seq:
        result ^= num
    return result


result = odd_int([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])
print(result)  # Output: 4