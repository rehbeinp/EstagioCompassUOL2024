'''Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a 
lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
liga(): muda o ligada da lâmpada para ligada
desliga(): muda o ligada da lâmpada para desligada
esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
Para testar sua classe:
Ligue a Lampada
Imprima: A lâmpada está ligada? True
Desligue a Lampada
Imprima: A lâmpada ainda está ligada? False'''

class Lampada:
    def __init__(self, ligada):
        self.ligada=ligada
    
    def liga (self):
        self.ligada=True
    
    def desliga (self):
        self.ligada=False
        
    def esta_ligada(self):
        return self.ligada
        
if __name__=="__main__":
    l1=Lampada(None)
    l1.liga()
    print(f"A lâmpada está ligada? {l1.esta_ligada()}")
    l1.desliga()
    print (f"A lâmpada está ligada? {l1.esta_ligada()}")
