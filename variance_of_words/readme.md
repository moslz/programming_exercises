## Word Length Variance Calculator

This Python function calculates the variance of the lengths of words in a list.

### Usage

1. Provide a list of words as input.
2. Call the `variance` function with the list of words.

Considering "Hi" and "World":

X is { 2, 5 } with P(X = 5) = 1/2 and P(X = 2) = 1/2.
So E[X] = 5 x 1/2 + 2 x 1/2 = 3.5 and the standard formula for variance is E[(X - u)^2] so 1/2 x (2-3.5)^2 + 1/2 x (5 - 3.5)^2 = 2.25 or you can calculate with the other formula E[X^2] - E[X]^2 = (5^2 x 1/2 + 2^2 x 1/2) - 3.5^2 = 2.25

Example:

```python
words = ["Hi", "World"]
words_variance = variance(words)
print (words_variance)
```

The function returns the variance, rounded to a maximum of 4 decimal places.
