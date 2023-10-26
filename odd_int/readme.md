# Odd-Occurrence Finder

## Description

This Python function, `odd_int(seq)`, is written to solve the problem of finding the integer that appears an odd number of times in a given array of integers.

## Usage
The function uses the XOR (exclusive or) operation to find the odd-occurring integer in the array. It iterates through the array and XORs all the elements together. Since XORing an integer with itself results in 0 and XORing 0 with any integer results in the integer itself, the end result is the integer that appears an odd number of times.

To use this function, simply pass an array of integers as an argument, and it will return the integer that fits the criteria. 

```python
result = odd_int([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])
print(result)  # Output: 4
```

## Examples

Here are a few examples to illustrate the function's usage:

- Input: `[4]`
  - Output: `4`
- Input: `[1, 1, 5]`
  - Output: `5`
- Input: `[0, 1, 0, 1, 0]`
  - Output: `0`

## License

This project is open-source and available under the [MIT License](LICENSE).
