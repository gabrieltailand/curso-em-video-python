'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''

# Função área
def area(largura, comprimento):
    a = largura * comprimento
    print('-' *30)
    print(f'A área é {a}m²')
    print('-' * 30)


# Programa Principal
area(largura = float(input('Largura (m): ')), comprimento = float(input('Comprimento (m): ')))
