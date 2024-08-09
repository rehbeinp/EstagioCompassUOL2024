import names
import random
import time

random.seed(40)
qtd_nomes_unicos=3000
qtd_nomes_aleatorios=10000000

lista=[]

for i in range (qtd_nomes_unicos):
    lista.append(names.get_full_name())
    
print(" Gerado {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]

for i in range(0,qtd_nomes_aleatorios):
    dados.append(random.choice(lista))

with open("nomes_aleatorios.txt", "a") as arquivo:
    for nome in dados:
        arquivo.write(f"{nome}\n")
arquivo.close()