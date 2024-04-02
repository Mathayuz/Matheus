'''Lorenzo Henrique Zanetti ra133076
    Matheus Cenerini Jacomini ra134700'''


'''código recursivo para obter fatoriais na conta que diz o elemento da pirâmide'''
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)


'''cálculo do elemento com o número da linha e coluna'''
def elemento_pascal(linha, coluna):
    elemento = int(fatorial(linha)/(fatorial(coluna)*fatorial(linha - coluna)))
    return elemento


'''função que imprime cada linha da pirâmide até a linha de número desejado (considerando que as linhas começam em 0,
inserindo o valor 5, 6 linhas são imprimidas.)'''
def triangulo_pascal(quantidade_de_linhas):
    if quantidade_de_linhas == 0:
        return print([1])
    elif quantidade_de_linhas < 0:
        return print("Número Inválido!")
    else:
        triangulo_pascal(quantidade_de_linhas - 1)
        linha = []
        for i in range(quantidade_de_linhas + 1):
            elemento = elemento_pascal(quantidade_de_linhas, i)
            linha.append(elemento)
        return print(linha)


'''Código Principal'''
x = int(input(f'Insira o número de linhas da pirâmide de Pascal à serem impressos: '))
triangulo_pascal(x - 1)
