**`findding nth digit in a number` Function**

The `findDigit` function is a JavaScript function that helps to retrieve the nth digit of a number `num`, counting from right to left. 

a few essential considerations:

1. **Absolute Value Handling:** Regardless of whether `num` is positive or negative, the function treats it as a positive value when searching for the nth digit.

2. **Valid Input Check:** It checks if `nth` is a positive integer. If `nth` is not a valid input, the function returns -1.

3. **Leading Zeros:** The function understands that numbers like 42 and 00042 are equivalent, so it correctly returns the nth digit from the right side while considering leading zeros.

**Usage:**

To use the `findDigit` function, provide two arguments:
- `num`: The number from which you want to extract the nth digit.
- `nth`: The position of the digit you wish to retrieve, counting from right to left.

**Examples:**

```javascript

console.log(findDigit(4569, 2));     // Output: 2
console.log(findDigit(-2825, 3));   // Output: 8
console.log(findDigit(0, 20));      // Output: 0
console.log(findDigit(68, 0));      // Output: -1

```

**Note:**

- If `nth` is 0 or a negative number, or if it exceeds the number of digits in `num`, the function returns -1 to indicate an invalid request.
