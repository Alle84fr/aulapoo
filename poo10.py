palavra = input("Digite uma palavra: ")

vog = dict(a=0, e=0, i=0, o=0, u=0)

for letra in palavra:
          if letra in vog:
                    vog[letra] += 1

print(vog)