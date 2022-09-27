"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

ilhas = ['terceira', 'graciosa', 'pico', 'faial', 'sjorge']
vendas = []

def divisores(num):
    zeros = 0
    for n in range(1, num + 1):
        if num % n == 0:
            zeros += 1  # zeros = zeros + 1
    return zeros
def declarar_lista(casas):
    for x in range(casas):
        vendas.append(0)

if __name__ == '__main__':
    vendas = []
    total = 0
    for ilha in ilhas:
        vendas.append(float(input(f'Insira as vendas para {ilha}')))
    print(f'vendas={vendas}')

    menor = vendas [0]
    maior = vendas [0]
    for x in range(1, len(vendas)):
        if vendas[x] < menor:
            menor = vendas[x]
        if vendas[x] > maior:
            maior = vendas[x]
    v = vendas.sort()
    print(v)
    print(f'maior é {maior} e o menor {menor}')
    print(f'vendas = {sum(vendas)}')

