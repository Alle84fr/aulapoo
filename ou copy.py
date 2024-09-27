from getpass import getpass


lista=[]

palavraChave = getpass("digite uma palavra: ")
tam = len(palavraChave)
for letra in range(len(palavraChave)):
          lista.append(letra)
          rep = let.count()

print(f"chance{chance}")

print(lista)
print(len(lista))
palavra=tam*["_"]
print(palavra)
digitados=[]


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

