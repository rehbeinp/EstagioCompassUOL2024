import random

lista=[]
while True:
    numero = random.randint(1,500) #chamando a função random que gera números aletório e salvando o resultado em uma variavel
    if numero not in lista:        # verificando se o número já não está na lista
        lista.append(numero)       # adicionando na lista caso não esteja
    tamanho=len(lista)             # chamando a função len para e guardadno o tamanho da lista em uma variável
    
    if tamanho==250:               # quebrando o while caso o tamanho for igual a 250
        break
    

lista.reverse()                   # revertendo os elementos da lista
print(lista)                      # imprimindo o resultado
