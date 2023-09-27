def narcissistic(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_digits

    return total == number