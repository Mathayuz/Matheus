'''Lorenzo Henrique Zanetti ra133076
    Matheus Cenerini Jacomini ra134700'''


'''função para obter por input em formato de float os valores (garantindo que sejam positivos) e 
retorná-los numa lista ordenada para trabalhar com eles depois'''
def lados(x):
    lados = []
    contagem = 0
    while contagem < x:
        l = float(input("Insira um valor positivo: "))
        if l <= 0:
            print('Valor Inválido!')
        else:
            lados.append(l)
            contagem += 1
    # Função de ordenação: (ela troca a posição do elemento por todos os menores que ele em ordem crescente,
    # levando o número à sua posição ordenada.)
    for i in range(len(lados)):
        for j in range(i+1, len(lados)):
            if lados[i] >= lados[j]:
                # temp = variável temporária
                temp = lados[i]
                lados[i] = lados[j]
                lados[j] = temp
    return lados



'''Verificar se os três lados fornecidos formam um triângulo e retornar em boolean'''
def triangulo(lista):
    lista.sort()
    if lista[2] < lista[1] + lista[0] and lista[2] > lista[1] - lista[0]:
        return True
    else:
        return False



'''Classificar o tipo de triângulo à partir de uma lista de lados ordenada'''
def classificacao(lados_lista):
    A = lados_lista[2]
    B = lados_lista[1]
    C = lados_lista[0]
    if A**2 == B**2 + C**2:
        print('\nO triângulo é retângulo!')

    elif A**2 > B**2 + C**2:
        print('\nO triângulo é obtusângulo!')

    elif A**2 < B**2 + C**2:
        print('\nO triângulo é acutângulo!')



'''Calcular a área do triângulo'''
def area(lados_lista):
    a = lados_lista[2]
    b = lados_lista[1]
    c = lados_lista[0]
    S = (a + b + c) / 2
    area = (S*(S-a)*(S-b)*(S-c))**(1/2)
    return area


'''código principal'''
lista_lados = lados(3)
triangulo = triangulo(lista_lados)
if triangulo == False:
    print("Os lados não formam um triângulo!")
else:
    classificacao(lista_lados)
    print(f'A sua área é: {area(lista_lados)}')
    