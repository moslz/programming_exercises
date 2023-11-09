**Find-S Algorithm Implementation**

### Overview
This Python script implements the Find-S algorithm for concept learning. The algorithm finds the most specific hypothesis that fits positive examples in a training dataset.

### How to Use
1. Define your training data as a list of lists, with '1' indicating positive examples and '0' for negative examples.
2. Run the script, and it will output the progress of the Find-S algorithm for each training instance.
3. The final output provides the maximally specific hypothesis that fits all positive examples.

### Example
```python
# Define your training data
training_data = [
    ['Monday', 'No', 'Easygoing', 'Evening', '1'],
    ['Monday', 'No', 'Annoyed', 'Evening', '0'],
    ['Saturday', 'Yes', 'Easygoing', 'Lunchtime', '0'],
    ['Monday', 'No', 'Easygoing', 'Morning', '1']
]

# Run the Find-S algorithm
hypothesis = find_s_algorithm(training_data)

# Output the maximally specific hypothesis
print("Maximally specific hypothesis:", hypothesis)
```
