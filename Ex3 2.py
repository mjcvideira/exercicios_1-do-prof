"""
Complete o programa

Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random

        ini = float(input('Insira o primeiro número '))
        fim = float(input('Insira o segundo número '))

r1 = random.randint((ini), (fim))

    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """


if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        ini = float(input('Insira o primeiro número '))
        fim = float(input('Insira o segundo número '))
        print()

