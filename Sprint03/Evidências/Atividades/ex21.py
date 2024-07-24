'''Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as 
habilidades de voar e emitir som.
Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, 
conforme o modelo a seguir.
Imprima no console exatamente assim:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu'''

class Passaro:
    def __init__ (self, voar, emitir_som):
        self.voar=voar
        self.emitir_som=emitir_som
        
class Pardal(Passaro):
    def __init__(self, voar, emitir_som):
        self.voar=voar
        self.emitir_som=emitir_som
        return print("Pardal")
        
    def voando(self):
        return (print("Voando..."))
    
    def emitindo(self):
        return(print("Piu Piu"))
    
class Pato(Passaro):
    def __init__(self, voar, emitir_som):
        self.voar=voar
        self.emitir_som=emitir_som
        return print("Pato")
        
    def voando(self):
        return(print("Voando..."))
    
    def emitindo(self):
        return(print("Quack Quack"))
    
if __name__=="__main__":
    p1=Pardal(True, True)
    p1.voando()
    print("Paradal emitindo som...")
    p1.emitindo()
    p2=Pato(True, True)
    p2.voando()
    print("Pato emitindo som...")
    p2.emitindo()
        
        