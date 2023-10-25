def sum_of_intervals(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for interval in intervals[1:]:
        current = merged_intervals[-1]
        if interval[0] <= current[1]:
            current = (current[0], max(current[1], interval[1]))
            merged_intervals[-1] = current
        else:
            merged_intervals.append(interval)

    total_length = sum(interval[1] - interval[0] for interval in merged_intervals)
    return total_length
