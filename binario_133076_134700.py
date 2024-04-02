"""Lorenzo Henrique Zanetti ra:133076
   Matheus Cenerini Jacomini ra:134700"""

def conversorbinario(n):
    if n < 0:
        return "O número deve ser positivo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    resto = n % 2
    return resto + (conversorbinario(n // 2)) * 10


inteiro = int(input("Digite um número inteiro para converter para binário: "))
binario = conversorbinario(inteiro)
print(binario)

"""Por exemplo, para n = 3, retornamos [1 + (conversorbinario(1)) * 10], onde (conversorbinario(1)) retorna 1, e portanto
temos 1 + 1 * 10 que é 11, que também é a representação binária do inteiro "3"."""

"""Por exemplo, para n = 4, retornamos [0 + (conversorbinario(2)) * 10], onde (conversorbinario(2)) retorna
[0 + (conversorbinario(1)) * 10], onde (conversorbinario(1)) retorna 1, e portanto temos que (conversorbinario(2))
retorna [0 + 1 * 10] que é 10, logo (conversorbinario(4)) retorna [0 + 10 * 10], que é 100, que também é a representação
binário do inteiro "4"."""