def parse_numbers(string):
    def parse_single_word(word):
        if word in word_to_number:
            return word_to_number[word]
        elif '-' in word:
            compound_numbers = word.split('-')
            return sum(parse_single_word(w) for w in compound_numbers)
        else:
            return 0

    word_to_number = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }

    words = string.replace('-', ' ').replace(' and ', ' ').split()
    total = 0
    current_number = 0

    for word in words:
        if word == 'hundred':
            current_number *= 100
        elif word == 'thousand':
            total += current_number * 1000
            current_number = 0
        elif word == 'million':
            total += current_number * 1000000
            current_number = 0
        else:
            current_number += parse_single_word(word)

    return total + current_number

print(parse_numbers("fifty"))
print(parse_numbers("seven hundred eighty-three thousand nine hundred and nineteen"))