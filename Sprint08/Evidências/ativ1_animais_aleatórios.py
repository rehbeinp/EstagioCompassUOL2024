animais=["coruja", "vaca", "cachorro", "gato", "boi", "golfinho", "baleia", "gaviao", "hipopotamo", "elefante", "hiena", "leao", "onca-pintada", "pato", "mareco", "morcego", "cavalo", "cabra","camelo", "flamingo"]
animais.sort()


with open("animais.csv", "a") as arquivo:
    for animal in animais:
        print(animal)
        arquivo.write(f"{animal}\n")
arquivo.close()