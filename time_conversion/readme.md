the given python function takes a non-negative integer representing the number of seconds and returns the time in a readable format of (HH:MM:SS). 

```python
def format_time(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input out of range")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```
**Output format:**

- HH (Hours): Padded to 2 digits, within the range of 00 - 99.
- MM (Minutes): Padded to 2 digits, within the range of 00 - 59.
- SS (Seconds): Padded to 2 digits, within the range of 00 - 59.
- The maximum time represented by this function does not exceed 359999 seconds, which is equivalent to 99 hours, 59 minutes, and 59 seconds.
