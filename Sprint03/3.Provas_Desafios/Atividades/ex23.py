'''
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e 
retorne a subtração dos dois (resultados negativos são permitidos).
Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5
imprima:
Somando: 4+5 = 9
Subtraindo: 4-5 = -1
'''

class Calculo:
    def __init__(self):
        pass
        
    def soma(X,Y):
        s=X+Y
        return print(f"Somando: {X}+{Y} = {s}")
    
    def subtrai(X,Y):
        sub=X-Y 
        if sub<0: 
            sub==0
        return print(f"Subtraindo: {X}-{Y} = {sub}")

if __name__=="__main__":
    (Calculo.soma(4, 5))
    (Calculo.subtrai(4, 5))
    

    
    