lista=[]

palavraChave = "conjunto"

for letras in palavraChave:

          lista.append(letras)
print(lista)
print(len(lista))
palavra=["_","_","_","_","_","_","_","_"]

digitados=[]

chance = 8

print(*palavra, sep=" " )
print()

while True:

          
          chute = input(" Adivinhe uma letra do alfabeto: ")

          for i in range(len(lista)):

                    if chute == lista[i]:

                              palavra[i]=chute


          digitados.append(chute)

          print("\n Letras digitadas", *digitados, sep=" ")
          print(*palavra, sep="  ")

          chance -= 1

          print(f"\n você tema mais {chance} \n")

          if chance == 0: 
                    print(" A pavrala correta era CONJUNTO \n")
                    break                   

          if palavra == lista:
                    print("Aeeeee, você adivinhou a palvra")
                    break

