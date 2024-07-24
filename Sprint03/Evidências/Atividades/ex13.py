'''Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Dica: leia a documentação da função open(...)'''

with open(r"C:\Users\teste\OneDrive\Área de Trabalho\estagio UOL\Curso Pyhton\PyhtonCodigos\atividades\arquivo_texto.txt", "+r",encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha=linha.strip("\n")
        linha=linha.strip()
        print(linha)
