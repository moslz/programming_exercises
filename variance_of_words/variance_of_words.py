def variance(words):
    
    total_length = 0
    word_count = len(words)

    for word in words:
        total_length += len(word)

    mean_x = total_length / word_count
    sum_of_squared_differences = 0

    for word in words:
        squared_difference = (len(word) - mean_x) ** 2
        sum_of_squared_differences += squared_difference

    variance_x = sum_of_squared_differences / word_count

    return round(variance_x, 4)


words = ["Hi", "World"]
words_variance = variance(words)
print (words_variance)
