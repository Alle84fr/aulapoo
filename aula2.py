# forca - com cond de vitória, cond derrota - possui regras e
# palavra  principal separada por letras- criando uma lista de letras corretas
# se a letra digitada está na lista, aparece, caso não aparece -  e menos uma chance
# 1° palavra, 2°lista de letras corretas 3°input chance 4°coparar a lista

vitória = False 
chance = 6
palavra = "tentativa"
letCorreta = []
chutes = []

for let in palavra:
          letCorreta.append(let)

while True:
          for i in letCorreta:
                    if i in chutes: print(i, end=" ")
                    else : 
                              print("_", end=" ")
                              chance -= 1

                    tent = input("Digite uma letra: ")
                    chutes.append(tent)
                    if tent not in chutes:

                    if chance == 0: break



