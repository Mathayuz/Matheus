"""Lorenzo Henrique Zanetti ra:133076
   Matheus Cenerini Jacomini ra:134700"""


'''Função pa obter incomodam n vezes'''
def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n-1)
    

'''função que retorna a letra da música'''
def elefantes(n):
    if n < 1:
        return ''
    elif n == 1:
        return 'Um elefante incomoda muita gente'
    elif n == 2:
        return elefantes(n-1) + f'\n{n} elefantes {incomodam(n)}muito mais'
    else:
        return elefantes(n-1) + f'\n{n-1} elefantes incomodam muita gente\n{n} elefantes {incomodam(n)}muito mais '
    

'''código para input'''
x = int(input('Até quantos elefantes? '))
print(elefantes(x))
