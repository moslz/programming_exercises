def regressionLine(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(x_i**2 for x_i in x)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))

    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n

    return round(a, 4), round(b, 4)

result1 = regressionLine([25, 30, 35, 40, 45, 50], [78, 70, 65, 58, 48, 42])
print(result1)