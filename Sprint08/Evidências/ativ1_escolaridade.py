import random
esc=[]

qtd_nomes_aleatorios=10000000
lista=["medio", "fundamental", "superior"]

for i in range(0,qtd_nomes_aleatorios):
    esc.append(random.choice(lista))

with open("escolaridade.txt", "a") as arquivo:
    for nome in esc:
        arquivo.write(f"{nome}\n")
arquivo.close()
