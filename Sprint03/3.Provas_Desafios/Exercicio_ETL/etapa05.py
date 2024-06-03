'''Lista dos autores ordenada por Total Gross (receita bruta) em ordem decrescente'''

output = []

t=open(r"C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\etapa05.txt", '+a',encoding='utf-8')
f = open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\actors.csv', '+r',encoding='utf-8' ) #abrir o arquivo em read universal mode
for line in f:
    cells = line.split( "," )
    if cells [0]=='"Robert Downey':
        cells[1]=cells[2]
        cells[2]=cells[3]
        cells[3]=cells[4]
        cells[4]=cells[5]
        cells[5]=cells[6]
    if cells[1]!="Total Gross":
        filmes=float(cells[1])
        output.append((cells[0],cells[1]))
output.sort(key=lambda x: x[1], reverse=True)

for i in output:
    t.write(f"{i[0]:25} - {i[1]}\n")
    print(f"{i[0]:25} - {i[1]}", end='\n')

f.close()
t.close()