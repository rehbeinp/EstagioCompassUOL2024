'''A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários.
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos.
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map
'''
from functools import reduce

def calcula_saldo(lancamentos):

    def valor(lancamento):
        quant, tipo = lancamento                             # salva o valor e o tipo, pegando essas informações de lancamento
        return quant if tipo=="C" else -quant                #retorna o valor dependendo do tipo

    total=reduce(lambda x, y: x+y, map(valor, lancamentos))  # soma o total com o reduce, da lista gerada pelo map com a funçaõ valor
    return total                                              



lancamento= [
    (200,'D'),
    (300,'C'),
    (100,'C')]
print(calcula_saldo(lancamento))
