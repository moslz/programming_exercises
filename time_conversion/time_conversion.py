def format_time(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Input out of range")

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print (format_time(1200))