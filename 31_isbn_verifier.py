"""
    example: 3-598-21508-8
    if X in digit  X == 10
"""

def is_valid(isbn):
    numbers = list(isbn.replace("-", ""))
    if len(numbers) !=10: return False
    if numbers[-1] == 'X': numbers[-1] = "10"
    if not all([c.isdigit() for c in numbers]): return False
    return sum(int(x)*y for x,y in zip(numbers, range(10, 0, -1))) % 11 == 0
