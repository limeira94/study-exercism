def is_triangle(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0:
        return a + b >= c and a + c >= b and b + c >= a
    return False

def equilateral(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a == b == c
    return False

def isosceles(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a == b or a == c or b == c
    return False

def scalene(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a != b and a != c and b != c
    return False 