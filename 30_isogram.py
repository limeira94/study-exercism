"""
    up-to-date
"""

def is_isogram(string):
    string_lower = string.lower().replace(" ", "")
    for idx, letter in enumerate(string_lower):
        count_letter = string_lower.count(letter)
        if count_letter != 1 and string_lower[idx] != '-':
            return False
    return True
    
    
if __name__ == '__main__':
    print(is_isogram("six-year-old"))
