import random
pais=[]

qtd_nomes_aleatorios=10000000
lista=["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Guiana Francesa", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]

for i in range(0,qtd_nomes_aleatorios):
    pais.append(random.choice(lista))

with open("pais.txt", "a") as arquivo:
    for nome in pais:
        arquivo.write(f"{nome}\n")
arquivo.close()