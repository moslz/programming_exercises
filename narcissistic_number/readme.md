# Narcissistic Number Checker

This Python function determines whether a given positive integer is a narcissistic number in base 10. A narcissistic number is one that is equal to the sum of its own digits, each raised to the power of the number of digits in the number.

## Usage

To check if a number is narcissistic, call the `narcissistic` function with the number as an argument. It will return `True` if the number is narcissistic and `False` if it's not.

Example:
```python
result = is_narcissistic(153)  # Returns True
result = is_narcissistic(1652)  # Returns False
