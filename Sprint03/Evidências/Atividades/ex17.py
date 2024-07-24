'''Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida 
dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
'''


def funcao(l=[]):
    lista1=[]
    lista2=[]
    lista3=[]
    tamanho=len(l)
    tamanho=tamanho//3
    for elemento in l:
        if len(lista1)!=tamanho:
            lista1.append(elemento)
        elif len(lista2)!=tamanho:
            lista2.append(elemento)
        elif len(lista3)!=tamanho:
            lista3.append(elemento)
    return lista1, lista2, lista3

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = funcao(lista)

print(lista1, lista2, lista3)
