def square(number): 
    if number >= 1 and number <= 64:
        if number == 1:
            return 1
        else:
            return 2 * square(number - 1)
    raise ValueError("square must be between 1 and 64")

def total():
    count = 0
    for i in range(1, 65):
        count += square(i)
    return count

