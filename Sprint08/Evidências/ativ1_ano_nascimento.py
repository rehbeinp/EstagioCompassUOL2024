import random
pais=[]

qtd_nomes_aleatorios=10000000

for i in range(0,qtd_nomes_aleatorios):
    pais.append(random.randint(1945,2010))

with open("ano_nasciemento.txt", "a") as arquivo:
    for nome in pais:
        arquivo.write(f"{nome}\n")
arquivo.close()