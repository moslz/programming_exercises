
# Sum of Intervals
Python function, `sum_of_intervals`, calculates the sum of non-overlapping interval lengths from a list of intervals.

## Usage

```
intervals = [(1, 5), (6, 10), (11, 15)]
total_length = sum_of_intervals(intervals)
print(total_length)  
```
## How it Works

1. Sort the intervals by their starting points.
2. Merge overlapping intervals.
3. Calculate the total length by summing the lengths of non-overlapping intervals.

## Example

For the input `[(1, 5), (6, 10), (11, 15)]`, the function returns 9 because the non-overlapping intervals are `[1, 5], [6, 10], and [11, 15]`, and their total length is 9.
