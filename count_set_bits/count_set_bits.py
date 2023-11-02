def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1

    return count

result = count_set_bits(223)
print(result) 