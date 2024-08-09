'''Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se
 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou 
 Ímpar: e o número correspondente (um linha para cada número lido).

'''
numeros=[]

for n in range(3):
    numeros.append(n)
    if n%2==0:
        print (f"Par: {n}")
    else:
        print (f"Ímpar: {n}")



    
    