import random

def gerar_cpf():

return "".join([str(random.randint(0, 9)) for _ in range(9)])

torcedor = dict(judo=0, volei=0, ginastica=0, surf=0, nenhum=0)
l
p = 0
while p <= 15:
          escolha = input("Qual esporte assistiu j para judô, v vôlei, g para ginástica e s para surfe: ")
          print(" ")
          if escolha == "j":
                    esporte = "judo"
                    torcedor["judo"] += 1
          elif escolha == "v":
                    esporte = "volei"
                    torcedor["volei"] += 1 
          elif escolha == "g":
                    esporte = "ginastica"
                    torcedor["ginastica"] += 1
          elif escolha == "s":
                    esporte = "surf"
                    torcedor["surf"] += 1  
          else:
                    esporte = "nenhum"
                    torcedor["nenhum"] += 1                 
          p += 1



pr = torcedor.get("judo")/15 + torcedor.get("surf")/15
pr1 = (torcedor.get("judo") + torcedor.get("surf") + torcedor.get("ginastica") + torcedor.get("volei"))/15
pr2 = (torcedor.get("judo") + torcedor.get("surf"))/15
pr3 = ((torcedor.get("judo") + torcedor.get("surf") + torcedor.get("ginastica") + torcedor.get("volei")) - torcedor.get("nenhum"))/15

print(f" probabilidade para judo ou surf {pr} \n")
print(f" probabilidade todos {pr1} \n")
print(f" probabilidade minino 2 {pr2} \n")
print(f" probabilidade nenhum {pr3} \n")
print(f" total de respostas {torcedor}")


          