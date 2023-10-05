def stat(strg):
    if not strg:
        return ""
    
    race_times = strg.split(', ')
    
    race_times_seconds = []
    for time in race_times:
        h, m, s = map(int, time.split('|'))
        total_seconds = h * 3600 + m * 60 + s
        race_times_seconds.append(total_seconds)
    
    race_times_seconds.sort()
    range_seconds = race_times_seconds[-1] - race_times_seconds[0]
    average_seconds = sum(race_times_seconds) // len(race_times_seconds)
    median_seconds = race_times_seconds[len(race_times_seconds) // 2]
    if len(race_times_seconds) % 2 == 0:
        median_seconds = (race_times_seconds[len(race_times_seconds) // 2 - 1] + median_seconds) // 2
    
    def seconds_to_hms(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}|{m:02}|{s:02}"
    
    range_str = seconds_to_hms(range_seconds)
    average_str = seconds_to_hms(average_seconds)
    median_str = seconds_to_hms(median_seconds)
    
    return f"Range: {range_str} Average: {average_str} Median: {median_str}"


result = stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17")
print(result)

