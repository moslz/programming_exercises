def digital_root(n):

    if n < 10:
        return n

    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10

    return digital_root(digit_sum)

print(digital_root(16))       # Output: 7
print(digital_root(942))      # Output: 6
print(digital_root(132189))   # Output: 6
