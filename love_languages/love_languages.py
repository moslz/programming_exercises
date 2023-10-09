import random

def love_language(partner, weeks):

    LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]
    response_counts = {}

    for lang in LOVE_LANGUAGES:
        response_counts[lang] = 0

    for _ in range(weeks * 7):
        for lang in LOVE_LANGUAGES:
            response = partner.response(lang)
            if response == "positive":
                response_counts[lang] += 1

    main_language = max(response_counts, key=response_counts.get)
    
    return main_language


class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang

    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85:
                return 'positive'
            else:
                return 'neutral'
        else:  # language != self.main
            if r < 0.15:
                return 'positive'
            else:
                return 'neutral'

def run_tests():
    weeks = 6
    partner = TestPartner('touch')
    result = love_language(partner, weeks)
    print("Test result for 'touch':", result)
    assert result == 'touch'

    partner = TestPartner('gifts')
    result = love_language(partner, weeks)
    print("Test result for 'gifts':", result)
    assert result == 'gifts'

if __name__ == "__main__":
    run_tests()

