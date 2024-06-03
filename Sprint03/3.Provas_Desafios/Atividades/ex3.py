'''Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você 
deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range()'''
for i in range(1, 101):
    soma=0
    for n in range(1, 101):
        if i%n==0:
            soma=soma+1
        else:
            pass
    if soma==2:
        print(i)
