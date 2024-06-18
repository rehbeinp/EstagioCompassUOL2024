'''Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e 
high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.'''

lista=[]
dif=[]
with open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\projetos\Sprint04\atividades\number.txt', "+r",encoding='utf-8') as arquivo:
    dados = [int (linha.strip()) for linha in arquivo]

def teste(a):
    if a not in dif:
        return a

dif=list(map(teste, dados))

for n in dados:
    if n not in lista:
        lista.append(n)

pares = filter(lambda x: x % 2 == 0, dif)

ordenados = sorted(pares, key=lambda x: -x)
maiores=ordenados[:5]
soma=sum (maiores)
print(maiores)
print(soma)