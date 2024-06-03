'''Ator/atriz com maior média de bilheteria bruta por filme considerando a coluna "Average per Movie"'''


output = []
ator=m=filmes=0
t=open(r"C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\etapa03.txt", '+a',encoding='utf-8')
f = open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\actors.csv', '+r',encoding='utf-8' ) #abrir o arquivo em read universal mode
for line in f:
    cells = line.split( "," )
    if cells [0]=='"Robert Downey':
        cells[1]=cells[2]
        cells[2]=cells[3]
        cells[3]=cells[4]
        cells[4]=cells[5]
        cells[5]=cells[6]
    if cells[3]!="Average per Movie":
        filmes=float(cells[3])
        if filmes>m:
            m=filmes
            ator=cells[0]
t.write(f"{ator} possui a maior média de bilheteria bruta por filme, que é {m}.")
f.close()
t.close()
print(f"{ator} possui a maior média de bilheteria bruta por filme, que é {m}.")