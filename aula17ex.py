class Pessoa:
          def __init__(self, identificador:int, nome:str):
                    self._identificador = identificador
                    self._nome = nome
                    print(f"A pessoa {self._nome} tem o id {self._identificador}")

class PessoaFica(Pessoa):
          def __init__(self, cpf:str, rg:str, dentificador:int, nome:str):
                    self._rg= rg
                    self._cpf=cpf
                     #sempre colocar todos os parâmetros
                    super().__init__(dentificador:int, nome:str)
                    print(f" cpf: {self._cpf} e rg:{self._rg}")


print(....*10)

class PessoaJuridica(Pessoa):
          def.__init__(self, cnpj:str,identificador:int, nome:str ):
                    self._cnpj = cnpj
                    super()__init__(identificador:int, nome:str)
                    print(f" cnpj: {self._cnpj}")

#principal


ser = Pessoa("Kalome", 123456)
serfis = 