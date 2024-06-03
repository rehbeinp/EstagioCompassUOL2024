'''Crie uma classe Avião que possua os atributos modelo, y, w e z.
Defina o atributo w de sua classe , de maneira que todas as instâncias de sua classe avião sejam da w “azul”.
Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.
Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
“O avião de modelo “x”: velocidade máxima de “y”, z para “z” passageiros e é da w “w”.
Sendo x, y, z e w cada um dos atributos da classe “Avião”.
Valores de entrada:
modelo BOIENG456: velocidade máxima 1500 km/h: z para 400 passageiros: w Azul
modelo Embraer Praetor 600: velocidade máxima 863km/h: z para 14 passageiros: w Azul
modelo Antonov An-2: velocidade máxima de 258 Km/h: z para 12 passageiros: w Azul'''

class Aviao:
    def __init__(self, x, y, z,  w="azul"):
        self.w=w
        self.x=x
        self.y=y
        self.z=z
        
    def modelo(self):
        return print(self.x)
    
    def velocidade(self):
        return  print(self.y)
    
    def capacidade(self):
        return print(self.z)
    
    def cor(self):
        if self.w=="azul": self.w="azul"
        return self.w
    
    
if __name__=="__main__":
    a1=Aviao("BOIENG456" , 1500, 400, "azul")
    a2=Aviao("Embraer Praetor 600", 863, 14, "azul")
    a3=Aviao("Antonov An-2", 258, 12, "azul")
    print (a1)
    print(f"O avião de modelo {a1.x}: velocidade máxima de {a1.y} km/h: capacidade para {a1.z} passageiros: cor {a1.w}.")
    print(f"O avião de modelo {a2.x}: velocidade máxima de {a2.y} km/h: capacidade para {a2.z} passageiros: cor {a2.w}.")
    print(f"O avião de modelo {a3.x}: velocidade máxima de {a3.y} km/h: capacidade para {a3.z} passageiros: cor {a3.w}.")

    
        
        