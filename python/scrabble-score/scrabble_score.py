def score(word):
    letter_values = {
        1: 'aeioulnrst',
        2: 'dg',
        3: 'bcmp',
        4: 'fhvwy',
        5: 'k',
        8: 'jx',
        10: 'qz'
    }

    score = 0
    for i in word.lower():
        for letter_value, letters in letter_values.items():
            if i in letters:
                score += letter_value

    return score
