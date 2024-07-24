'''Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será 
uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções:
len
filter
lambda
'''

def conta_vogais(texto:str):

    pequeno=texto.lower()
    vogais=list(filter(lambda x: x=="a" or x=="e" or x=="i" or x=="o" or x=="u", pequeno))
    return len(vogais)


print(conta_vogais("Catupiri"))