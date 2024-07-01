'''Quantidade de aparições dos filmes na coluna # Movie'''



output = []
filme_quant=[]

t=open(r"C:\Users\Paula Rehbein\Desktop\estagio UOL\projetos\EstagioC_UOL\Sprint03\3.Provas_Desafios\Exercicio_ETL\actors.csv", '+a',encoding='utf-8')
f = open(r'C:\Users\Paula Rehbein\Desktop\estagio UOL\projetos\EstagioC_UOL\Sprint03\3.Provas_Desafios\Exercicio_ETL\actors.csv', '+r',encoding='utf-8' ) #abrir o arquivo em read universal mode
for line in f:
    cells = line.split( "," )
    if cells [0]=='"Robert Downey':
        cells[1]=cells[2]
        cells[2]=cells[3]
        cells[3]=cells[4]
        cells[4]=cells[5]
        cells[5]=cells[6]
    if cells[4]!="#1 Movie":
        filme=cells[4]
        output.append(cells[4])
for fil in output:
    repetidos = output.count(fil)
    if (fil, repetidos) not in filme_quant:
        filme_quant.append((fil,repetidos))
n=0
for i in filme_quant:
    n=n+1
    t.write(f"{n} - O filme {i[0]} aparece {i[1]} vez(ses) no dataset.\n")   ### colocar quebra de linha
    print(f"{n}- O filme {i[0]} aparece {i[1]} vez(ses) no dataset.", end='\n')

f.close()
t.close()