'''Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
É o arquivo estudantes.csv de seu exercício.
Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão
O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao 
formato descrito a seguir:
Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
round
map
sorted
'''

import csv
estudantes=[]
with open(r'C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\projetos\Sprint04\atividades\estudante.csv', "+r",encoding='utf-8') as arquivo:
    #dados = [(linha.strip()) for linha in arquivo]
    tabela = csv.reader(arquivo, delimiter=',')


    for n in tabela:

        notas=[]
        maiores=[]
        notas.append((n[-1]))
        notas.append((n[-2]))
        notas.append((n[-3]))
        notas.append((n[-4]))
        notas.append((n[-5]))
        inteiros=list(map(int, notas))
        ordenada=sorted(inteiros, reverse=True)
        maiores.append(ordenada[0])
        maiores.append(ordenada[1])
        maiores.append(ordenada[2])
        media=(sum(maiores))/3
        media=round(media, 2)
        estudantes.append((n[0], maiores, media))

estudantes.sort()
for n in estudantes:
    print(f"Nome: {n[0]} Notas: {n[1]}  Média: {n[2]}")