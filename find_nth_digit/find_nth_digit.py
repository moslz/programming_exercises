def find_nth_digit(num, nth):
    if nth <= 0:
        return -1
    
    num = abs(num)
    num_str = str(num)
    index = len(num_str) - nth  
    
    if 0 <= index < len(num_str):
        nth_digit = int(num_str[index])
        return nth_digit
    else:
        return 0
    
result = find_nth_digit(789, 2)
print(result)
