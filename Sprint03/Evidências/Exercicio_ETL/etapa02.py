'''Média da receita da bilheteria bruta dos principais filmes, considerando todos os atores.'''


output = []
media=m=filmes=0
t=open(r"C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\etapa02.txt", '+a',encoding='utf-8')
f = open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\Exercicio_ETL\actors.csv', '+r',encoding='utf-8' ) #abrir o arquivo em read universal mode
for line in f:
    cells = line.split( "," )
    if cells [0]=='"Robert Downey':
        cells[1]=cells[2]
        cells[2]=cells[3]
        cells[3]=cells[4]
        cells[4]=cells[5]
        cells[5]=cells[6]
    if cells[5]!="Gross\n":
        filmes=float(cells[5])
    output.append( (filmes ) ) 
    m=m+1
media=sum(output)//m
    
t.write(f"Média de bilheteria dos princípais filmes de todos os atores é {media}.")
f.close()
t.close()
print(f"Média de bilheteria dos princípais filmes de todos os atores é {media}.")
