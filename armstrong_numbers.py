def is_armstrong_number(number):
    numero_str = str(number)
    soma = 0
    for i in numero_str:
        soma += int(i) ** len(numero_str)
    return soma == number


if __name__ == '__main__':
    print(is_armstrong_number(153))