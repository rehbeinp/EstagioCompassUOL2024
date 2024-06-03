'''Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']'''
def lista_sem_repet(lista):
    conjunto = set(lista)
    lista_nao_repete = list(conjunto)
    return lista_nao_repete


lista_original = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_nao_repet = lista_sem_repet(lista_original)
print(lista_nao_repet)
