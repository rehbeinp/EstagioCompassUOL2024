'''Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"
'''

def fucao(p):
    soma=0
    p=p.split(",")
    for n in p:
        n=int(n)
        soma=n+soma
    return soma

palavra=fucao("1,3,4,6,10,76")
print(palavra)
