'''Lorenzo Henrique Zanetti ra133076
    Matheus Cenerini Jacomini ra134700'''


'''Função para calcular o fatorial necessário para a próxima conta'''
def fatorial(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial



'''obter o ângulo do cosseno'''
x = float(input("Ângulo em radianos (número inteiro) do cosseno à ser calculado: "))

'''Cálculo do cosseno: no laço do while é usado a função pronta do cosseno para aproximar
com mais exatidão o número ao seu real valor, matendo a precisão no dentro dos valores desejados (0.001)'''

from math import cos
cosseno = 1
contador = 1
divisor = 2
sinal = -1

while cosseno < cos(x) - 0.001 or cosseno > cos(x) + 0.001:
    cosseno += (sinal*((x**divisor)/fatorial(divisor)))
    divisor += 2
    sinal *= -1
    contador += 1

print(f'\nO cosseno calculado utilizando a função importada do math: {cos(x)}')
print(f'O cosseno calculado pelo método proposto é: {cosseno}, que foi calculado em {contador} termos.\n')