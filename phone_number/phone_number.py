def phone_number(n):
    if len(n) != 10:
        return "Invalid input, the list should contain 10 integers."

    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
    return phone_number

number2 = phone_number([5, 5, 5, 1, 2, 3, 9, 8, 7, 0])
print(number2)  # Output: (555) 123-9870 