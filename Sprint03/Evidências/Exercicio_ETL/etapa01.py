'''Ator/Atriz com maior quantidade de filmes e a quantidade'''

output = []
maior=m=filmes=0
t=open(r"C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\etapa01.txt", '+a',encoding='utf-8')
f = open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\actors.csv', '+r',encoding='utf-8' ) #abrir o arquivo em read universal mode
for line in f:
    cells = line.split( "," )
    if cells [0]=='"Robert Downey':
        cells[1]=cells[2]
        cells[2]=cells[3]
    output.append( ( cells[ 0 ], cells[ 2 ] ) )
    if cells[2]!="Number of Movies":
        filmes=float(cells[2])
        if filmes > m:
            m=filmes
            maior=(cells[0],cells[2])
t.write(f"Ator com maior quantidade de filmes é {maior[0]}, com {maior[1]} filmes.")
f.close()
t.close()
print(f"Ator com maior quantidade de filmes é {maior[0]}, com {maior[1]} filmes.")
