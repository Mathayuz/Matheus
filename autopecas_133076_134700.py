"""Lorenzo Henrique Zanetti ra:133076
   Matheus Cenerini Jacomini ra:134700"""

import random as rnd


# Criar tabela, as funções funcionam para qualquer número de produtos / lojas
tabela = []
for linha in range(10):
    vetor = []
    for coluna in range(10):
        vetor.append(rnd.randint(1,100))
    tabela.append(vetor)


# Mostrar tabela
print('Colunas = lojas \nLinhas = produtos')
for i in tabela:
    print(i)

# Calcula a média aritmética de um vetor
def mediaaritmetica(vetor):
    soma = 0
    for elemento in vetor:
        soma += elemento
    media = round(soma/(len(vetor)),2)
    return media


# Determina o maior elemento de um vetor e seu indice
def maior(lista):
    maior = lista[0]
    indice = -1
    indice_final = 0
    for elemento in lista:
        indice += 1
        if elemento > maior:
            maior = elemento
            indice_final = indice
    return maior, indice_final

'''Função que retorna a média de vendas de cada produto numa lista'''
def media_produto(tabela):
    media_produtos = []
    for i in range(len(tabela)):
        media_produtos.append(mediaaritmetica(tabela[i]))
    return media_produtos

'''Função que retorna a média de vendas em cada loja numa lista'''
def media_loja(tabela):
    media_lojas = []
    for i in range(len(tabela[0])):    #função for para acessar cada lista de produtos
        loja = []
        for lista in tabela:        #função para acessar o item que representa vendas de cada loja por produto
            loja.append(lista[i])
        media_lojas.append(mediaaritmetica(loja))
    return media_lojas

'''Função que retorna a quantidade total de vendas por loja numa lista'''
def venda_loja(tabela):
    venda_lojas = []
    for i in range(len(tabela[0])):
        loja = 0
        for lista in tabela:
            loja += lista[i]
        venda_lojas.append(loja)
    return venda_lojas


'''Código para print'''
print('-'*50, '\nMédia dos produtos:')
medias_produtos = media_produto(tabela)
for i in range(len(tabela)):
    print(f'A média de vendas do produto {i+1} é: {medias_produtos[i]}')


print('-'*50, '\nMédia das lojas:')
medias_lojas = media_loja(tabela)
for i in range(len(medias_lojas)):
    print(f'A média de vendas na loja {i+1} é: {medias_lojas[i]}')


print('-'*50)
maior = maior(venda_loja(tabela))
print(f'A loja {maior[1] + 1} foi a que mais vendeu, com {maior[0]} vendas')
print('-'*50)
