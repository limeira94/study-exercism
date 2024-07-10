"""
    Number é 15
    Divisores de 15: 1, 3, 5
    15 // 1 = 15
    15 // 3 = 5
    15 // 5 = 3
    
"""

def classify(number):
    if number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    list_numbers = []
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            list_numbers.append(divisor)
            divisor += 1
        else:
            divisor += 1
    soma = sum(list_numbers)
    if soma == number:
        return 'perfect'
    elif soma > number:
        return 'abundant'
    return 'deficient'
    



if __name__ == '__main__':
    print(classify(15))    