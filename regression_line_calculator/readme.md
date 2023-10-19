Linear regression line calculator

given is a Python function that calculates the linear regression line from two lists of coordinates. The function takes two lists, `x` and `y`, where `x` represents the x-coordinates of the points and `y` represents the corresponding y-coordinates.

The linear regression line is represented as:

```
y = a + bx
```

where `a` is the intercept and `b` is the slope.

**Function:**

```python
def regressionLine(x, y):
    # Your code here
    pass
```

**Input:**

- `x`: A list of x-coordinates.
- `y`: A list of corresponding y-coordinates.

**Output:**

- A tuple containing two elements - the intercept `a` and the slope `b`, rounded to four decimal places.

**Example Usage:**

```python

result1 = regressionLine([25, 30, 35, 40, 45, 50], [78, 70, 65, 58, 48, 42])
print(result1)  # Expected Output: (114.381, -1.4457)

```
