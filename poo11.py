letras = dict(primeira="a", segunda="b", quarta="d", setima="g", decima="j", decima1="k", decima4="n", decima9="s", videsima1="u")

while True:

          valor1 = input("Digite uma letra ou 0 para sair: ")
          tem = False

          for posicao, letra in letras.items():
                    if valor1 == letra: 
                              print(f"A letra {valor1} está na posição {posicao}")
                              break
                   
                            

          if valor1 == 0: break