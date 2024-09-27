class Veiculo:
          def__init__(self, marca, modelo, )
          

class Carro(Veiculo):
          #def__init__(parametro):
          #super () chama o construtor da classe veículo, que é como se fosse função/construtor da super classe (OU COPIAR TODO MÉTODO)
          #porta é característica de alguns veículos, não todos
          #a herança pode ser funcionalidades básicaS
          # se carro tivesse uma sub classe, deveria por o carro como super
          def__init__(self, marca, modelo, placa, portas): 
          super()__init__(marcar, modelo, placa) #não tem self porque não está definindo, só coloca quando está definindo
          self.portas=portas

#cria um único objeto que possui dois tipo - carro que é veículo

          def exibir(self):
                    print("-----------------")
                    print("Marca": self.marca)
                    print("portas": self.portas)
#principal
#criando o objeto carro
#exibir informa as infirmações de caRRO
carros =Carro("ford", "Ka", "aaa1336", 4)
carro.exibir()
#OS ATRIBUTOS PUBLICOS, SE FOR PRIVADO DEVE FAZER OUTRA FORMA
# SE NÃO PASSAR PARAMETRO, QUALQUER UM DÁ ERRO


class Anima:
def fazer_som(self):
          print("emite som")

class Cachoirro(Anima):
def fazer_som(self):
          print("emite som")
          super() fazer_som()
          print("mia")
cachrro = 

resposta seria (emite som miau)
