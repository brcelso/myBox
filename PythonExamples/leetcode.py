"""
A program that converts a Roman numeral to an integer.
"""

ROMAN_NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def roman_to_int(roman_numeral: str) -> int:

    result = 0
    for i, numeral in enumerate(roman_numeral):
        if i> 0 and ROMAN_NUMERALS[numeral] > ROMAN_NUMERALS[roman_numeral[i - 1]]:
            result += ROMAN_NUMERALS[numeral] - 2 * ROMAN_NUMERALS[roman_numeral[i - 1]]
        else: 
            result += ROMAN_NUMERALS[numeral]
    return result

TEST_CASES = [
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),

]

for test_input, expected in TEST_CASES:
    result = roman_to_int(test_input)
    print(result, result == expected)