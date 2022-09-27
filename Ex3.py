"""
Complete o programa

Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random

def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros

def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)

if __name__ == '__main__':
    while True:
        try:
            quantos = int(input('Quantos?'))
            break
        except:
            print('valores validos')
    while True:
        try:
            ini = int(input('valora inicial'))
            fim = int(input('valor final?'))
            if fim < ini:
                print('o valor final nao pode ser que o inicial')
                continue
            break
        except:
            print('insere valores validos')

    for num in range(quantos):
        numero = get_random(ini, fim)
        print(numero)
        if numero % 2 == 0:
            out1 = f'o numero {numero} é par'
        else:
            out1 = f'o numero {numero} é impar'
        if divisores(numero) == 2:
            out2 = 'E é PRIMO'
        else:
            out2 = 'e nao e primo'
        print(f'{out1} {out2}')

