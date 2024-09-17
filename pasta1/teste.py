from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    try:
        num_fracs = int(input('Número de frações: '))
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido para o número de frações.")
        exit(1)

    for _ in range(num_fracs):
        while True:
            frac_input = input("Digite a fração (numerador denominador): ")
            try:
                numerator, denominator = map(int, frac_input.split())
                fracs.append(Fraction(numerator, denominator))
                break
            except ValueError:
                print("Erro: Por favor, insira dois números inteiros separados por espaço.")
            except ZeroDivisionError:
                print("Erro: O denominador não pode ser zero.")

    result = product(fracs)
    print("Resultado:", *result)


'''import re
import os
import random

os.system("clear")
for _ in range(100):
    cpf=''
    for i in range(9):
        cpf += str(random.randint(0,9))
    #cpf = input("Digite seu CPF: ")
    #cpf = re.sub(r'[^0-9]', "", cpf)

    if len(cpf) == 9:
        nove_digits = cpf[:9]

        # Calcula o primeiro dígito verificador
        contador_regres1 = 10
        resultado1 = 0
        for i in nove_digits:
            resultado1 += int(i) * contador_regres1
            contador_regres1 -= 1
        digito_1 = (resultado1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        # Calcula o segundo dígito verificador
        dez_digits = nove_digits + str(digito_1)
        contador_regres2 = 11
        resultado2 = 0
        for i in dez_digits:
            resultado2 += int(i) * contador_regres2
            contador_regres2 -= 1
        digito_2 = (resultado2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_conferido = f'{nove_digits}{digito_1}{digito_2}'
        print(cpf_conferido)
    else:
        print("Digite um CPF com 11 dígitos (apenas números)")'''
        